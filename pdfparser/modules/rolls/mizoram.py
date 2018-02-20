from .base import Reader, Patterns, GeneralInfo

__all__ = ['MizoramPDF']


class MizoramPatterns(Patterns):

	part_patterns = dict(
		main=r'Page2\n(.*)\nSUMMARY OF ELECTORS',
		addition=None,
		correction=None,
		deletion=None,
	)

	box_patterns = dict(
		main=r'(\d+\n(Father|Husband|Mother)(.*?(?=\n\d+\n(Father|Husband|Mother))|.*))',
		deletion=None
	)

	general_patterns = dict(
		state=r'STATE *\([A-Z]\d+\) *([^\n]+)',
		acName=[
			r'\n\d{6}\n[^\n]+\n[^\n]+\n([^\n]+)',
			r'([^\n]+)(?=\nSubdivision\nPincode)'
		],
		partNo=r'(?<=\nTotal\n)(\d+)',
		year=r'Roll Identification:\n(\d+)',
		mainTown=r'\nTotal\n\d+\n[^\n]+\n([^\n]+)',
		mandal=r'\nPincode\n([^\n]+)',
		policeStation=r'\nPincode\n[^\n]+\n([^\n]+)',
		district=r'\nTotal\n\d+\n[^\n]+\n[^\n]+\n([^\n]+)',
		stationName=r'\d+\n\d+ -\n\d+ -\n([^\n]+)',
		stationAddress=r'(?<=\nTotal\n)\d+\n[^a-z]+\n(.*?)(?=(\n\d+){6})',
		netMale=r'\n\d+\n(\d+)\n\d+\n\d+\n\d+\n\d+\n(?!Roll Identification:)',
		netFemale=r'\n\d+\n\d+\n(\d+)\n\d+\n\d+\n\d+\n(?!Roll Identification:)',
		netTotal=r'\n\d+\n\d+\n\d+\n(\d+)\n\d+\n\d+\n(?!Roll Identification:)'
	)

	elector_patterns = dict(
		number=r'^(\d+)',
		name=r'(?<=[Mm]ale\n)(.*?)(?=\nName :\n)',
		relativeName=r'(?<=\'s\nName :\n)(.*?)(?=\n([Ff]emale|[Mm]ale)\n)',
		house=r'(?<=\nSex :\n)(.*?)(?=[A-Z]{1,5}[0-9/]+)',
		age=r'Age *: *(\d+)',
		sex=r'([Ff]emale|[Mm]ale)'
	)


class MizoramGeneral(GeneralInfo):

	merged_patterns = True


class MizoramPDF(Reader):

	pat = MizoramPatterns()

	def __init__(self, path):
		super(MizoramPDF, self).__init__(path, cls_general=MizoramGeneral)
