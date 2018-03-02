import os
from collections import namedtuple

# Environment
APP_NAME = 'pdfparser'
APP_DESC = '''\
Parse PDF Indian electoral rolls to a CSV.'''
APP_CMD = APP_NAME.lower()
APP_PATH = os.path.dirname(__file__)
with open(os.path.join(APP_PATH, 'VERSION'), 'r') as f:
	APP_VERSION = f.read().strip()
	APP_NAME_WITH_VERSION = ' '.join([APP_NAME, APP_VERSION]).strip()

# Log settings
LOG_FILE = os.path.join(APP_PATH, 'logs/{}.log'.format(APP_NAME.lower()))
LOG_MAX_FILE_SIZE = 52428800  # 50MB
LOG_FILE_BACKUP_COUNT = 10
LOG_TIME_FORMAT = '%d/%m/%Y %I:%M:%S %p'

# Output & file
TRACK_FILE_NAME = '.{}'.format(APP_NAME.lower())
OUTPUT_FILE_TS = '%Y%m%d-%H%M%S'
OUTPUT_FILE = os.path.join(APP_PATH, 'output/Parsed-{}.csv')
OutputRow = namedtuple(
	'OutputRow',
	'number id elector_name father_or_husband_name has_husband house_no age sex ac_name part_no year state filename \
main_town police_station mandal revenue_division district pin_code polling_station_name polling_station_address \
net_electors_male net_electors_female net_electors_third_gender net_electors_total'
)
