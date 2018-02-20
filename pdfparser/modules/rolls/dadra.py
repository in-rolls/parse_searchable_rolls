from .base import Reader, Patterns

__all__ = ['DadraPDF']


class DadraPatterns(Patterns):

	part_patterns = dict(
		main=r'Page2(.*?)(?=\d+\. SUMMARY OF ELECTORS)',
		addition=None,
		correction=None,
		deletion=None,
	)

	box_patterns = dict(
		main=r'(?<=\n)(\d+\n(?=Father|Husband|Mother)(.*?(?=\n\d+\n(?=Father|Husband|Mother))|.*))',
		deletion=None
	)

	general_patterns = dict(
		state=r'([^\na-z]+)$',
		partNo=r'(?<=4 . NUMBER OF ELECTORS\n)[^\n]+\n(\d+)',
		year=r'Year of Revision\n: (\d+)',
		stationName=r'\n\d+ , ([^\na-z]+)(?=\n)',
		netMale=r'(?<=\nTotal\n)(\d+)',
		netFemale=r'(?<=\nTotal\n)\d+\n(\d+)',
		netTotal=r'(?<=\nTotal\n)\d+\n\d+\n(\d+)'
	)

	elector_patterns = dict(
		number=r'^(\d+)',
		name=r'Age :\n\d+\n([^\n]+)',
		relativeName=r'Age :\n\d+\n[^\n]+\n([^\n]+)',
		house=r'([^\n]+)(?=\n[A-Z]{1,5}[0-9/]+)',
		age=r'(?<=Age :\n)(\d+)',
		sex=r'(?<=\'s Name\n)([^\n]+)(?=\n\d+\n)'
	)


class DadraPDF(Reader):

	pat = DadraPatterns()

	def __init__(self, path):
		super(DadraPDF, self).__init__(path)
