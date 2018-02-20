import csv
try:
	from helpers import isfile
except ImportError:
	from os.path import isfile


class CsvWriter:

	def __init__(self, path, header=None, encoding=None, delimiter=',', quote='"', firstrow=0, newline=''):
		self.file = path
		self.header = header
		self.encoding = encoding
		self.delimiter = delimiter
		self.quote = quote
		self.firstrow = firstrow
		self.newline = newline
		self.__add_header()

	def __add_header(self):
		if not isfile(self.file):
			if self.firstrow > 0:
				for i in range(self.firstrow):
					self.append([])
			if self.header is not None:
				self.append(self.header)

	def write(self, rows):
		with open(self.file, 'w', newline=self.newline, encoding=self.encoding) as fp:
			writer = csv.writer(fp, delimiter=self.delimiter, quotechar=self.quote)
			writer.writerows(rows)

	def append(self, rows, multi=False):
		with open(self.file, 'a', newline='', encoding=self.encoding) as fp:
			writer = csv.writer(fp, delimiter=self.delimiter, quotechar=self.quote)
			if multi:
				writer.writerows(rows)
			else:
				writer.writerow(rows)
