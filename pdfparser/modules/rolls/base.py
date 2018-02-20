import re
from functools import partial
from collections import OrderedDict
from ..pdf import ParsePDF, ParsePDFConvertError
from .errors import RollParseError
from helpers import basename, oneline

__all__ = ['Patterns', 'Reader', 'Elector', 'GeneralInfo']


class Patterns:

	def __init__(self):
		self.patterns = OrderedDict(
			p_main=self.__compile(r'Page3(.*?)(?=SUPPLEMENT\sDETAILS)'),
			p_addition=self.__compile(r'ADDITIONS?\sLIST(.*?)(?=N(umber|o\.)\sof\sAdditions)'),
			p_correction=self.__compile(r'CORRECTIONS?\sLIST(.*?)(?=N(umber|o\.)\sof\sCorrections)'),
			p_deletion=self.__compile(r'DELETIONS?\sLIST(.*?)(?=N(umber|o\.)\sof\sDeletions)'),
			b_main=None,
			b_addition=None,
			b_correction=None,
			b_deletion=self.__compile(r'([A-Z]{1,5}[0-9]+)'),
			g_state=None,
			g_acName=None,
			g_acStatus=None,
			g_partNo=None,
			g_year=None,
			g_mainTown=None,
			g_policeStation=None,
			g_pinCode=self.__compile(r'\n(\d{6})\n'),
			g_mandal=None,
			g_revenueDivision=None,
			g_district=None,
			g_stationName=None,
			g_stationAddress=None,
			g_netMale=None,
			g_netFemale=None,
			g_netThird=None,
			g_netTotal=None,
			e_number=None,
			e_id=self.__compile(r'([A-Z]{1,5}[0-9/]+)'),
			e_name=None,
			e_house=None,
			e_age=None,
			e_sex=None,
			e_relativeName=None,
			e_relativeType=self.__compile(r'(Father|Husband|Mother)')
		)
		self.parse()

	def parse(self):
		for type_ in ('part', 'box', 'general', 'elector'):
			pat_attr = '%s_patterns' % type_
			if hasattr(self, pat_attr):
				patterns = getattr(self, pat_attr)
				if isinstance(patterns, dict):
					setter = getattr(self, 'set_%s' % pat_attr)
					setter(**patterns)

	@staticmethod
	def __compile(pattern):
		return re.compile(pattern, flags=re.DOTALL)

	def __get_keys(self, ptype):
		keys = []
		for key in self.patterns:
			if key.startswith('%s_' % ptype):
				keys.append(key[2:])
		return keys

	def get_general_attrs(self):
		return self.__get_keys(ptype='g')

	def get_elector_attrs(self):
		return self.__get_keys(ptype='e')

	def get_parts(self):
		return self.__get_keys(ptype='p')

	def __load_pat(self, pattern, finder, key=None, merged=False):
		if isinstance(pattern, (list, tuple)):
			if not merged:
				for pat in pattern:
					ret = finder(pat)
					if ret:
						return ret
			else:
				ret = []
				for pat in pattern:
					found = finder(pat)
					if found and isinstance(found, str):
						ret.append(found)
				if ret:
					return ' '.join(ret)
		elif isinstance(pattern, dict):
			if key:
				if key in pattern:
					return self.__load_pat(pattern[key], finder, merged=merged)
				elif '*' in pattern:
					return self.__load_pat(pattern['*'], finder, merged=merged)
		else:
			ret = finder(pattern)
			if ret:
				return ret
		return None

	def __find(self, pattern, finder, default, key=None, merged=False):
		pattern = self.patterns[pattern]
		if pattern is not None:
			ret = self.__load_pat(pattern, finder, key, merged)
			if ret:
				return ret
		return default

	def __find_str(self, text, pattern, key=None, merged=False):
		def finder(pat):
			found = pat.findall(text)
			if found:
				return found[0][0] if isinstance(found[0], tuple) else found[0]
		return self.__find(pattern=pattern, finder=finder, default='', key=key, merged=merged)

	def __find_lst(self, text, pattern, key=None):
		def finder(pat):
			return list(map(lambda x: x[0] if isinstance(x, tuple) else x, pat.findall(text)))
		return self.__find(pattern=pattern, finder=finder, default=[], key=key, merged=False)

	def find_part(self, text, part):
		return self.__find_str(text=text, pattern='p_%s' % part)

	def find_boxes(self, text, part):
		return self.__find_lst(text=text, pattern='b_%s' % part)

	def find_general_attr(self, text, attr, merged=False):
		return self.__find_str(text=text, pattern='g_%s' % attr, merged=merged)

	def find_elector_attr(self, text, attr, key=None, merged=False):
		return self.__find_str(text=text, pattern='e_%s' % attr, key=key, merged=merged)

	def __read_pat(self, pattern):
		if isinstance(pattern, str):  # single-pattern
			return self.__compile(pattern)
		elif isinstance(pattern, (list, tuple)):  # multi-patterns
			return [self.__compile(p) for p in pattern]
		elif isinstance(pattern, dict):  # multi-patterns with key
			return {pk: self.__read_pat(pv) for pk, pv in pattern.items()}
		elif pattern is None:
			return None
		else:
			raise NotImplementedError('Unsupported pattern format: %r' % pattern)

	def __set_pat(self, ptype, **patterns):
		for key, pattern in patterns.items():
			key = '%s_%s' % (ptype, key)
			if key not in self.patterns:
				raise KeyError('Not supported key: %s' % key)
			self.patterns[key] = self.__read_pat(pattern)

	def set_part_patterns(self, **patterns):
		self.__set_pat('p', **patterns)

	def set_elector_patterns(self, **patterns):
		self.__set_pat('e', **patterns)

	def set_general_patterns(self, **patterns):
		self.__set_pat('g', **patterns)

	def set_box_patterns(self, **patterns):
		self.__set_pat('b', **patterns)


class Reader:

	pat = None

	def __init__(self, path, cls_elector=None, cls_general=None):
		try:
			parsed = ParsePDF(path)
		except (FileNotFoundError, EnvironmentError, ParsePDFConvertError) as exc:
			raise RollParseError(exc)
		else:
			if not parsed.has_data():
				raise RollParseError('Empty parsed data')
			self.file = parsed.pdf_file
			self._text = parsed.get_text()

		if not isinstance(self.pat, Patterns):
			raise AttributeError('Patterns instance not found')

		cls_general = cls_general or GeneralInfo
		self.general = cls_general(text=parsed.get_page(1), patterns=self.pat)
		if not self.general.has_data():
			raise RollParseError('Unable to parse/find General Info')

		cls_elector = cls_elector or Elector
		self.cls_elector = partial(cls_elector, patterns=self.pat)

		self.electors = OrderedDict()
		self.reverses = set()
		self.parse()

	@property
	def filename(self):
		return basename(self.file)

	def get_text(self):
		return self._text

	def has_data(self):
		return len(self.electors) > 0

	def parse(self):
		for part in self.pat.get_parts():
			self.parse_part(part)

	def parse_part(self, part):
		text = self.pat.find_part(self._text, part)
		if text:
			items = self.pat.find_boxes(text, part)
			task = partial(self.parse_elector, part=part) if part != 'deletion' else self.del_elector
			for item in items:
				task(item)

	def parse_elector(self, text, part):
		elector = self.cls_elector(text, part)
		if elector.has_data():
			self.electors[elector.number] = elector

	def del_elector(self, elector_id):
		found = None
		for key, item in self.electors.items():
			if item.id == elector_id:
				found = key
				break
		if found:
			self.electors.pop(found)


class Elector:

	reverses = None
	skiptxts = None
	husband = None
	merged_patterns = False

	def __init__(self, text, part, patterns):
		self.pat = patterns
		self._text = text
		self._part = part
		self.number = self.find('number')
		self.id = self.find('id')
		self.house = self.find('house')
		self.age = self.find('age')
		self.sex = self.find('sex')
		self.name = self.find('name')
		self.relative_name = self.find('relativeName')
		self.parse()

	@property
	def reversed(self):
		if self.reverses is not None:
			try:
				return self._part in self.reverses
			except TypeError:
				pass
		return False

	@property
	def skipped(self):
		if self.skiptxts is not None:
			try:
				for txt in self.skiptxts:
					if txt in self._text:
						return True
			except TypeError:
				pass
		return False

	def has_husband(self):
		if self.husband is None:
			return self.find('relativeType') == 'Husband'
		else:
			return self.find('relativeType') == self.husband

	def has_data(self):
		return not self.skipped and all([self.number, self.name])

	def get_text(self):
		return self._text

	def find(self, attr, alter=True):
		text = self.pat.find_elector_attr(
			text=self._text, attr=attr, key=self._part, merged=bool(self.merged_patterns))
		return oneline(text) if alter else text

	def parse(self):
		pass


class GeneralInfo:

	merged_patterns = False

	def __init__(self, text, patterns):
		self.pat = patterns
		self._text = text
		self.state = self.find('state')
		self.part_no = self.find('partNo')
		self.year = self.find('year')
		self.town = self.find('mainTown')
		self.police_station = self.find('policeStation')
		self.pin_code = self.find('pinCode')
		self.mandal = self.find('mandal')
		self.division = self.find('revenueDivision')
		self.district = self.find('district')
		self.station_name = self.find('stationName')
		self.station_addr = self.find('stationAddress')
		self.net_male = self.find('netMale')
		self.net_female = self.find('netFemale')
		self.net_third = self.find('netThird')
		self.net_total = self.find('netTotal')
		self.parse()

	@property
	def ac_name(self):
		name = self.find('acName')
		stat = self.find('acStatus')
		if name and stat:
			return name if stat in name else '%s (%s)' % (name, stat)
		return name

	def has_data(self):
		return all([self.state, self.part_no])

	def get_text(self):
		return self._text

	def find(self, attr, alter=True):
		text = self.pat.find_general_attr(text=self._text, attr=attr, merged=bool(self.merged_patterns))
		return oneline(text) if alter else text

	def parse(self):
		pass
