import logging
from logging.handlers import RotatingFileHandler
from helpers import timestamp
from globals import LOG_FILE, LOG_FILE_BACKUP_COUNT, LOG_MAX_FILE_SIZE, LOG_TIME_FORMAT

__all__ = ['log_configurer', 'LogFacility']


def log_configurer():
	root = logging.getLogger()
	root.setLevel(logging.WARNING)
	formatter = logging.Formatter(fmt='%(message)s')
	fileHandler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_MAX_FILE_SIZE, backupCount=LOG_FILE_BACKUP_COUNT)
	fileHandler.setFormatter(formatter)
	root.addHandler(fileHandler)


class LogFacility:

	def __init__(self, name=None):
		self.logger = logging.getLogger(name)

	def banner(self):
		banner = '\nLog started at: {:22}\n{}'.format(timestamp(LOG_TIME_FORMAT), '-' * 38)
		self.logger.warning(banner)

	def info(self, msg):
		self.logger.warning(msg)
		print(msg)

	def error(self, msg):
		msg = 'ERROR: %s' % msg
		self.logger.error(msg)
		print(msg)
