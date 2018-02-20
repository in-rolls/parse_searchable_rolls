from .base import Reader, Patterns

__all__ = ['MeghalayaPDF']


class MeghalayaPatterns(Patterns):

	part_patterns = dict(
		main=r'Page2\n(.*)\nSUMMARY OF ELECTORS',
		addition=None,
		correction=None,
		deletion=None,
	)

	box_patterns = dict(
		main=r'(\d+\nHouse No(.*?(?=\n\d+\nHouse No)|.*))',
		deletion=None
	)

	general_patterns = dict(
		state=r'\n[A-Z\d]+ - ([^\n]+)(?=\nPage 1 of \d+\n)',
		acName=r'([^\n]+)\n[^\n]+\n[^\n]+\n[^\n]+(?=\nPage 1 of \d+\n)',
		partNo=r'Net Electors\n\d+\n(\d+)',
		year=r'Year of Revision\n: (\d+)',
		mainTown=r'\n\d{6}\n[^\n]+\n(.*?)(?=\n[^\n]+\nPostOffice\n)',
		mandal=r'Main Village Town\n:\n([^\n]+)',
		policeStation=r'\n\d{6}\n([^\n]+)',
		district=r'\n\d+\.[A-Z ]+\n((?!\d+\.[A-Z ]+)[^\n]+)',
		stationName=r'\n\d+ +([^\n]+)(?=\n[A-Z]\d+ - [^\n]+)',
		stationAddress=r'\n\d+\.[A-Z ]+\n(?!\d+\.[A-Z ]+)[^\n]+\n(.*?)(?=[^\n]+\n\d+\n)',
		netMale=r'(\d+)\n\d+\n\d+\n\d+(?=\n\d{6}\n)',
		netFemale=r'(\d+)\n\d+\n\d+(?=\n\d{6}\n)',
		netThird=r'(\d+)\n\d+(?=\n\d{6}\n)',
		netTotal=r'(\d+)(?=\n\d{6}\n)'
	)

	elector_patterns = dict(
		number=r'^(\d+)',
		name=r'\nName :(.+?)\n(?=Father|Mother|Husband|Other)',
		relativeName=r'(?<=\'s Name :)(.+?)\n\d+(?=$|\n)',
		relativeType=r'(Father|Husband|Mother|Other)',
		house=r'House No : ([^\n]+)',
		age=r'(?<=\'s Name :).+?\n(\d+)(?=$|\n)',
		sex=r'Gender : ([^\n]+)'
	)


class MeghalayaPDF(Reader):

	pat = MeghalayaPatterns()

	def __init__(self, path):
		super(MeghalayaPDF, self).__init__(path)
