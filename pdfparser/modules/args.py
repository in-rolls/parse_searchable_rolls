from argparse import ArgumentParser
from .rolls import states
from helpers import timestamp, ispdf, isfile, isdir, dirname, filext
from globals import APP_DESC, APP_CMD, APP_NAME_WITH_VERSION, OUTPUT_FILE, OUTPUT_FILE_TS


def get_args():
    parser = ArgumentParser(description=APP_DESC, prog=APP_CMD)

    parser.add_argument('-f', '--file', metavar='FILE', help='path to the PDF file that is to be parsed')

    parser.add_argument('-d', '--dir', metavar='DIR', help='path to the directory containing the PDF files that are to be parsed')

    parser.add_argument('-s', '--state', metavar='STATE', help='state whose PDF rolls(s) are to be parsed')

    parser.add_argument('-l', '--lang', metavar='LANG', default='english', help='specify language used in parsing \
documents (default is English if not being specified)')

    parser.add_argument('-o', '--out', metavar='FILE', default=OUTPUT_FILE.format(timestamp(OUTPUT_FILE_TS)), help='\
specify output file for storing parsed result (must be \'.csv\' file). The default output file is \
\'Parsed-{timestamp}.csv\' and stored in the \'output\' directory')

    parser.add_argument('--resume', action='store_true', default=False, help='allows the parsing to be \
resumed later if the program is stopped unexpectedly or intentionally. Only takes effect if it is applied to a directory')

    parser.add_argument('--version', action='version', version=APP_NAME_WITH_VERSION)

    parser.add_argument('--all-states', action='store_true', default=False, help='show all the states that are supported and exit')

    args = parser.parse_args()

    if args.all_states:
        out = []
        chars = max(len(x) for x in states.keys())
        for state, langs in states.items():
            out.append('%-{}s : %s'.format(chars) % (state, ', '.join(langs)))
        parser.exit(message='States supported:\n%s\n' % '\n'.join(out))

    if not args.file and not args.dir or not args.state:
        parser.error('the following arguments are required: -f/--file or -d/--dir, -s/--state')

    if args.file and args.dir:
        parser.error('only accepts one of --file or --dir at a time')

    elif args.file:
        if not isfile(args.file):
            parser.error('file not found: %s' % args.file)
        if not ispdf(args.file):
            parser.error('file must be in PDF format')
        if args.resume:
            parser.error('parsing file does not allow --resume')

    elif args.dir:
        if not isdir(args.dir):
            parser.error('folder not found: %s' % args.dir)

    if args.state.lower() not in states:
        parser.error('unsupported state \'%s\'' % args.state)

    if args.lang and args.lang.lower() not in states[args.state.lower()]:
        parser.error('state \'%s\' does not have \'%s\' language' % (args.state, args.lang))

    if dirname(args.out) and not isdir(dirname(args.out)):
        parser.error('output folder does not exist: %s' % dirname(args.out))

    if filext(args.out).lower() != 'csv':
        parser.error('output file must be \'.csv\'')

    args.path = args.file or args.dir
    args.state = args.state.lower()
    args.lang = args.lang.lower()

    return args
