from argparse import ArgumentParser
from .rolls import ALL_STATES
from helpers import timestamp, ispdf, isfile, isdir, dirname, filext
from globals import APP_DESC, APP_CMD, APP_NAME_WITH_VERSION, OUTPUT_FILE, OUTPUT_FILE_TS


def get_args():
	parser = ArgumentParser(description=APP_DESC, prog=APP_CMD)

	parser.add_argument('-f', '--file', metavar='FILE', help='path to the specific PDF file to be parsed')

	parser.add_argument('-d', '--dir', metavar='DIR', help='path to directory containing the PDF files')

	parser.add_argument('-s', '--state', metavar='STATE', help='Name of state where PDF document(s) is/are published')

	parser.add_argument('-o', '--out', metavar='FILE', default=OUTPUT_FILE.format(timestamp(OUTPUT_FILE_TS)), help='\
Specify the output file for storing the results (must be \'.csv\' file). The default output file is \
\'Parsed-{timestamp}.csv\' located in \'output\' directory')

	parser.add_argument('--resume', action='store_true', default=False, help='Allows us to resume parsing if \
the program was stopped unexpectedly or intentionally. Only takes effect if. Only takes effect if directory is being parsed')

	parser.add_argument('--version', action='version', version=APP_NAME_WITH_VERSION)

	parser.add_argument('--all-states', action='store_true', default=False, help='show all supported states and exit')

	args = parser.parse_args()

	if args.all_states:
		parser.exit(message='States supported: %s\n' % ', '.join(ALL_STATES))

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

	if dirname(args.out) and not isdir(dirname(args.out)):
		parser.error('output folder does not exist: %s' % dirname(args.out))

	if filext(args.out).lower() != 'csv':
		parser.error('output file must be \'.csv\'')

	args.path = args.file or args.dir

	return args
