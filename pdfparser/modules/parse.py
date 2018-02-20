from . import rolls
from .track import Tracker
from .csv import CsvWriter
from .logger import LogFacility
from .rolls import RollParseError
from helpers import isdir, scanpdfs
from globals import OutputRow
from config import WRITE_ONLY_FILENAME

__all__ = ['RollParser']


class RollParser:

	def __init__(self, path, state, output, resume=False):
		try:
			name = state.split()[0].capitalize()
			self.reader = getattr(rolls, '%sPDF' % name)
		except AttributeError:
			raise ValueError('Unsupported state with name: %s' % state)
		self.pdfs = scanpdfs(path) if isdir(path) else [path]
		self.tracker = Tracker(path, output) if isdir(path) and resume else None
		self.writer = CsvWriter(path=self.tracker.output if self.tracker else output, header=OutputRow._fields)
		self.logger = LogFacility(self.__class__.__name__)
		self.__parse()
		if self.tracker is not None:
			self.tracker.cleanup()

	def __parse(self):
		count = 0
		for pdf in self.pdfs:
			count += 1
			# Skip if being found in tracker
			if self.tracker is not None:
				if self.tracker.found(item=pdf):
					self.logger.info('Skipped %s' % pdf)
					continue
			# Process PDF
			self.logger.info('Processing %s...' % pdf)
			try:
				# Read & parse PDF
				roll = self.reader(pdf)
			except RollParseError as exc:
				# Move forward if error found
				self.logger.error(exc)
				continue
			else:
				# Prepare list of parsed electors as rows for writing
				rows = []
				for elector in roll.electors.values():
					rows.append(OutputRow(
						number=elector.number,
						id=elector.id,
						elector_name=elector.name,
						father_or_husband_name=elector.relative_name,
						has_husband='yes' if elector.has_husband() else 'no',
						house_no=elector.house,
						age=elector.age,
						sex=elector.sex,
						ac_name=roll.general.ac_name,
						part_no=roll.general.part_no,
						year=roll.general.year,
						state=roll.general.state,
						filename=roll.filename if WRITE_ONLY_FILENAME else roll.file,
						main_town=roll.general.town,
						police_station=roll.general.police_station,
						mandal=roll.general.mandal,
						revenue_division=roll.general.division,
						district=roll.general.district,
						pin_code=roll.general.pin_code,
						polling_station_name=roll.general.station_name,
						polling_station_address=roll.general.station_addr,
						net_electors_male=roll.general.net_male,
						net_electors_female=roll.general.net_female,
						net_electors_third_gender=roll.general.net_third,
						net_electors_total=roll.general.net_total
					))
				# Write prepared rows of current PDF to output file
				if rows:
					self.writer.append(rows=rows, multi=True)
				# Keep done PDF in tracker for resuming check
				if self.tracker is not None:
					self.tracker.add(item=pdf)
					self.tracker.save()
				# Log done status
				self.logger.info('Done %s' % pdf)

		# Log if no file found
		if count == 0:
			self.logger.info('No PDF files found.')