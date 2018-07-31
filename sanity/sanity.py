#!/usr/bin/env python3

import os
import sys
import time
from functools import partial
from operator import itemgetter
from argparse import ArgumentParser, Namespace
from collections import Counter, OrderedDict
from libs import ElectoralCSV

__all__ = [
    'TestMethods',
    'read_electoral_csv',
    'print_all_tests',
    'test'
]

APP_NAME = 'sanity'
APP_PATH = os.path.dirname(__file__)
APP_CMD = os.path.basename(__file__)
APP_VERSION = 'v1.1'
APP_DESC = 'Check integrity of Electoral rolls data in CSV format parsed by pdfparser'

DATE_UPDATE = 'update: 01-May-2018'
VERSION_INFO = '{} {} ({})'.format(APP_CMD, APP_VERSION, DATE_UPDATE)
RELEASE_INFO = '''\
Release Notes:
--------------
v1.1:
  - Modified to be a CLI tool with input parameters
  - Revised verify_gender() to test_aggregation()
  - Revised verify_age() to test_age()
  - Revised verify_duplicated_ids() to test_duplication()
  - Revised verify_text_length() to test_txt_length()
  - Revised verify_id_length() to test_id_length()
  - Revised verify_pincode_length() to test_pin_length()
  - Revised verify_name_length() to test_name_length()
  - Revised verify_unique_text() to test_unique_txt()
  - Revised verify_unique_sex() to test_unique_sex()
  - Added test_unique_district(), test_unique_ac(), test_unique_mandal(), test_unique_town()
  - Revised so that it is compatible with IPython Notebook

v1.0:
  - Initial version
'''

ALL_TESTS = OrderedDict([
    ('duplication', 'test_duplication'),
    ('aggregation', 'test_aggregation'),
    ('age', 'test_age'),
    ('id-length', 'test_id_length'),
    ('pincode-length', 'test_pin_length'),
    ('name-length', 'test_name_length'),
    ('unique-sex', 'test_unique_sex'),
    ('unique-district', 'test_unique_district'),
    ('unique-acname', 'test_unique_ac'),
    ('unique-mandal', 'test_unique_mandal'),
    ('unique-town', 'test_unique_town'),
])

ALL_TESTS_TXT = '\n'.join(list(ALL_TESTS.keys()) + ['all']) + '\n'

DEFAULT_NAME_MIN_LENGTH = 3
DEFAULT_PIN_MIN_LENGTH = 6
DEFAULT_ID_MIN_LENGTH = 4
DEFAULT_MIN_AGE = 18
DEFAULT_MAX_AGE = 100


def get_test_func(test_name, args):
    assert isinstance(args, Namespace)
    func_name = ALL_TESTS[test_name]
    if 'verbose' in args:
        kwargs = {'verbose': args.verbose}
    else:
        kwargs = {'verbose': False}
    if test_name.endswith('-length'):
        attr = 'min_%s' % test_name.replace('-', '_')
        if attr in args:
            kwargs['minlength'] = getattr(args, attr)
    elif test_name == 'age':
        if 'minage' in args:
            kwargs['minage'] = args.minage
        if 'maxage' in args:
            kwargs['maxage'] = args.maxage
    return partial(getattr(TestMethods, func_name), **kwargs)


def get_args(*params):
    parser = ArgumentParser(description=APP_DESC, prog=APP_CMD)

    parser.add_argument('file', metavar='FILE', nargs='?', help='input CSV file parsed by pdfparser')

    parser.add_argument('--test', metavar='TEST_NAME', nargs='+', help='name of integrity check to be performed')

    parser.add_argument('--minage', metavar='AGE', type=int, default=DEFAULT_MIN_AGE,
                        help='minimum age when TEST_NAME is \'age\' (default is %d)' % DEFAULT_MIN_AGE)

    parser.add_argument('--maxage', metavar='AGE', type=int, default=DEFAULT_MAX_AGE,
                        help='maximum age when TEST_NAME is \'age\' (default is %d)' % DEFAULT_MAX_AGE)

    parser.add_argument('--min-id-length', metavar='LENGTH', type=int, default=DEFAULT_ID_MIN_LENGTH,
                        help='minimum length for TEST_NAME \'id-length\' (default is %d)' % DEFAULT_ID_MIN_LENGTH)

    parser.add_argument('--min-pincode-length', metavar='LENGTH', type=int, default=DEFAULT_PIN_MIN_LENGTH,
                        help='minimum length for TEST_NAME \'pincode-length\' (default is %d)' % DEFAULT_PIN_MIN_LENGTH)

    parser.add_argument('--min-name-length', metavar='LENGTH', type=int, default=DEFAULT_NAME_MIN_LENGTH,
                        help='minimum length for TEST_NAME \'name-length\' (default is %d)' % DEFAULT_NAME_MIN_LENGTH)

    parser.add_argument('--verbose', action='store_true', default=False,
                        help='display test results in more details')

    parser.add_argument('--all-tests', action='store_true', default=False,
                        help='list all supported integrity checks')

    parser.add_argument('--version', action='version', version=VERSION_INFO)

    parser.add_argument('--releases', action='store_true', default=False, help='display release notes and exit')

    args = parser.parse_args(*params)

    # Return release info
    if args.releases:
        parser.exit(message=RELEASE_INFO)

    # Return all tests supported
    if args.all_tests:
        parser.exit(message=ALL_TESTS_TXT)

    # Check file input
    if args.file is None:
        parser.error('the following argument is required: FILE')
    else:
        if os.path.isfile(args.file):
            if args.file[-3:] not in ('csv', 'CSV'):
                parser.error('Not a CSV file: %s' % args.file)
        else:
            parser.error('FILE does not exist: %s' % args.file)

    # Check input tests
    if args.test is None:
        parser.error('the following argument is required: --test TEST_NAME')
    else:
        tests = [i.lower() for i in args.test]
        args.test_methods = []
        if 'all' in tests:
            if len(tests) > 1:
                parser.error('does not accept multiple values when \'--test all\' is specified')
            for t in ALL_TESTS.keys():
                args.test_methods.append(get_test_func(t, args))
            args.test = list(ALL_TESTS.keys())
        elif set(tests) <= set(ALL_TESTS.keys()):
            for t in tests:
                args.test_methods.append(get_test_func(t, args))
            args.test = tests
        else:
            parser.error(
                'Unsupported TEST_NAME: %s (try \'--all-tests\' for more information)' %
                ', '.join(set(tests) - set(ALL_TESTS.keys()))
            )

    # Return parsed arguments
    return args


class TestMethods:
    @staticmethod
    def test_duplication(data, verbose=False):
        failed_files = []
        for file, rows in data.items():
            ids = [row.id for row in rows]
            unique_ids = set(ids)
            dup_ids = []
            if len(unique_ids) != len(ids):
                counter = Counter(ids)
                for id_, count in sorted(counter.items(), key=itemgetter(1), reverse=True):
                    if count > 1:
                        dup_ids.append((id_, count))
                failed_files.append(file)
                if verbose:
                    time.sleep(.2)
                    print('  + File "{}" has duplicated IDs: {}'.format(
                        file, ', '.join('{} (count: {})'.format(i, j) for i, j in dup_ids)))
        return failed_files

    @staticmethod
    def test_aggregation(data, verbose=False):
        failed_files = []
        for file, rows in data.items():
            doc_male = rows[0].net_electors_male or 0
            doc_female = rows[0].net_electors_female or 0
            doc_other = rows[0].net_electors_third_gender or 0
            doc_total = rows[0].net_electors_total or 0
            count_male = len(list(filter(lambda x: x.refined_sex == 'male', rows)))
            count_female = len(list(filter(lambda x: x.refined_sex == 'female', rows)))
            count_other = len(list(filter(lambda x: x.refined_sex == 'other', rows)))
            count_total = count_male + count_female + count_other
            matched = all([
                doc_male == count_male,
                doc_female == count_female,
                doc_other == count_other,
                doc_total == count_total
            ])
            if not matched:
                failed_files.append(file)
                if verbose:
                    time.sleep(.2)
                    print('  + File "%s" has unmatched aggregations:' % file)
                    print('    - Total electors: {} counted / {} documented:'.format(count_total, doc_total))
                    print('    - Total men: {} counted / {} documented'.format(count_male, doc_male))
                    print('    - Total women: {} counted / {} documented'.format(count_female, doc_female))
                    print('    - Total third gender: {} counted / {} documented'.format(count_other, doc_other))
        return failed_files

    @staticmethod
    def test_age(data, verbose=False, minage=DEFAULT_MIN_AGE, maxage=DEFAULT_MAX_AGE):
        failed_files = []
        for file, rows in data.items():
            wrong_ages = [row for row in rows if row.age < minage or row.age > maxage]
            if wrong_ages:
                failed_files.append(file)
                if verbose:
                    time.sleep(.2)
                    print('  + File "{}" has {} unreasonable ages: {}'.format(
                        file,
                        len(wrong_ages),
                        ', '.join('{} (age: {})'.format(row.id, row.age) for row in wrong_ages)
                    ))
        return failed_files

    @staticmethod
    def test_txt_length(data, attr, minlength, verbose=False):
        failed_files = []
        for file, rows in data.items():
            attrs = [getattr(row, attr) for row in rows]
            wrong_length = list(filter(lambda x: len(x) < minlength, attrs))
            if wrong_length:
                failed_files.append(file)
                if verbose:
                    time.sleep(.2)
                    print('  + File "{}" has {} unexpected "{}" length: {}'.format(
                        file,
                        len(wrong_length),
                        attr,
                        ', '.join('{} (len: {})'.format(i, len(i)) for i in wrong_length)
                    ))
        return failed_files

    @staticmethod
    def test_id_length(data, minlength=DEFAULT_ID_MIN_LENGTH, verbose=False):
        return TestMethods.test_txt_length(data, attr='id', minlength=minlength, verbose=verbose)

    @staticmethod
    def test_pin_length(data, minlength=DEFAULT_PIN_MIN_LENGTH, verbose=False):
        return TestMethods.test_txt_length(data, attr='pin_code', minlength=minlength, verbose=verbose)

    @staticmethod
    def test_name_length(data, minlength=DEFAULT_NAME_MIN_LENGTH, verbose=False):
        return TestMethods.test_txt_length(data, attr='elector_name', minlength=minlength, verbose=verbose)

    @staticmethod
    def test_unique_txt(data, attr, unique_count=1, verbose=False):
        failed_files = []
        for file, rows in data.items():
            attrs = [getattr(row, attr) for row in rows]
            uniques = Counter(attrs)
            if len(uniques) > unique_count:
                failed_files.append(file)
                if verbose:
                    failed = []
                    for index, item in enumerate(sorted(uniques.items(), key=itemgetter(1), reverse=True)):
                        if index >= unique_count:
                            failed.append('%s (count: %s)' % (item[0], item[1]))
                    time.sleep(.2)
                    print('  + File "{}" is having {} out of {} expected unique "{}": {}'.format(
                        file, len(failed), unique_count, attr, ', '.join(failed)))
        return failed_files

    @staticmethod
    def test_unique_sex(data, verbose=False):
        return TestMethods.test_unique_txt(data, attr='sex', unique_count=3, verbose=verbose)

    @staticmethod
    def test_unique_district(data, verbose=False):
        return TestMethods.test_unique_txt(data, attr='district', unique_count=1, verbose=verbose)

    @staticmethod
    def test_unique_ac(data, verbose=False):
        return TestMethods.test_unique_txt(data, attr='ac_name', unique_count=1, verbose=verbose)

    @staticmethod
    def test_unique_mandal(data, verbose=False):
        return TestMethods.test_unique_txt(data, attr='mandal', unique_count=1, verbose=verbose)

    @staticmethod
    def test_unique_town(data, verbose=False):
        return TestMethods.test_unique_txt(data, attr='main_town', unique_count=1, verbose=verbose)


def read_electoral_csv(file):
    print('Reading %s...' % file)
    parsed = ElectoralCSV(file)
    print('* Found state: %s (year: %s)' % (parsed.state, parsed.year))
    files = parsed.getdict(bykey='filename')
    print('* Found %s electoral files in state' % len(files))
    return files


def print_all_tests():
    print(ALL_TESTS_TXT)


def test(name, data, method=None, **kwargs):
    name = name.lower()
    if name not in ALL_TESTS.keys():
        raise ValueError('Unsupported test name: %s' % name)
    print('* Testing "%s"...' % name)
    if method is None:
        args = Namespace(**kwargs)
        method = get_test_func(name, args)
    failed = method(data=data)
    if failed:
        print('  --> %s/%s electoral files FAILED "%s" test: %s' %
              (len(failed), len(data), name, ', '.join(failed)))
    else:
        print('  --> PASSED')
    return failed


def main():
    # Read and prepare data
    args = get_args()
    files = read_electoral_csv(args.file)
    time.sleep(.5)

    # Do tests
    failed_tests = []
    failed_files = []
    for i, method in enumerate(args.test_methods):
        test_name = args.test[i]
        failed = test(name=test_name, data=files, method=method)
        if failed:
            failed_tests.append(test_name)
            failed_files.extend(failed)

    # Write summary
    if len(args.test) > 1:
        time.sleep(.5)
        print('\nSummary:\n--------')
        time.sleep(.5)
        if failed_tests:
            failed = set(failed_files)
            print('* {} FAILED: {}'.format('Tests were' if len(failed_tests) > 1 else 'Test was', ', '.join(failed_tests)))
            print('* {}/{} electoral files FAILED the tests: {}'.format(len(failed), len(files), ', '.join(failed)))
        else:
            print('* All tests PASSED!')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as exc:
        print('Error: %s' % exc)
        sys.exit(1)
