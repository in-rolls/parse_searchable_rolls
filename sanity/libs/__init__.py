import csv
from collections import namedtuple, defaultdict

__all__ = ['ElectoralFields', 'ElectoralCSV', 'ElectoralRow', 'read_csv', 'write_csv']


ElectoralFields = namedtuple(
    'ElectoralFields',
    'number id elector_name father_or_husband_name has_husband house_no age sex ac_name parl_constituency part_no year \
state filename main_town police_station mandal revenue_division district pin_code polling_station_name \
polling_station_address net_electors_male net_electors_female net_electors_third_gender net_electors_total change'
)


class ElectoralRow:
    bool_fields = ('has_husband',)
    num_fields = ('number', 'age', 'year', 'net_electors_male', 'net_electors_female', 'net_electors_third_gender',
                  'net_electors_total')
    gender_field = 'sex'

    def __init__(self, row):
        assert isinstance(row, (list, tuple))
        for index, cell in enumerate(row):
            field = ElectoralFields._fields[index]
            if field == self.gender_field:
                setattr(self, field, cell)
                self.refined_sex = self.refine(field, cell)
                continue
            setattr(self, field, self.refine(field, cell))

    @classmethod
    def refine(cls, field, value):
        if field in cls.bool_fields:
            return value.strip().lower() in ('yes', 'true', '1')
        elif field in cls.num_fields:
            try:
                return int(value)
            except ValueError:
                return 0
        elif field == cls.gender_field:
            value = value.strip().lower()
            if value in ('male', 'm'):
                return 'male'
            elif value in ('female', 'f'):
                return 'female'
            else:
                return 'other'
        return value


def read_csv(file, get_header=False, row_parser=None, match_header=None):
    with open(file, newline='') as fp:
        rows = []
        data = csv.reader(fp, delimiter=',', quotechar='"')
        header = None
        if row_parser is None:
            row_parser = lambda x: x
        for row in data:
            if row:
                if header is None:
                    header = row
                    if match_header is not None:
                        for col, field in enumerate(match_header):
                            try:
                                assert header[col] == field
                            except (AssertionError, IndexError):
                                raise FileExistsError('CSV error: missing field "%s" at column #%d' % (field, col + 1))
                    if not get_header:
                        continue
                rows.append(row_parser(row))
        return rows


def write_csv(file, rows, header=None):
    if header is not None:
        rows = [header] + rows
    with open(file, 'w', newline='') as fp:
        writer = csv.writer(fp, delimiter=',', quotechar='"')
        writer.writerows(rows)


class ElectoralCSV:
    def __init__(self, file):
        self.rows = read_csv(file, row_parser=ElectoralRow, match_header=ElectoralFields._fields)
        attrs = (
            'state',
            'year'
        )
        for attr in attrs:
            setattr(self, attr, getattr(self.rows[0], attr))

    def unique_rows(self):
        return (item for item in self if item.change != 'deleted')

    def len_unique_rows(self):
        return len(list(self.unique_rows()))

    def getdict(self, bykey, group=True, normalize=None):
        if group:
            ret = defaultdict(list)
            setter = lambda k, v: ret[k].append(v)
        else:
            ret = {}
            setter = lambda k, v: ret.__setitem__(k, v)
        getkey = bykey if callable(bykey) else lambda x: getattr(x, bykey)
        if normalize is None:
            normalize = lambda x: x
        assert callable(normalize)
        for row in self.unique_rows():
            setter(normalize(getkey(row)), row)
        return ret

    def __len__(self):
        return len(self.rows)

    def __iter__(self):
        return iter(self.rows)
