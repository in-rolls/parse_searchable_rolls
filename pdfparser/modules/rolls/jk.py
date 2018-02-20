from .base import Reader, Patterns

__all__ = ['JkPDF']


class JkPatterns(Patterns):

	part_patterns = dict(
		main=r'Page3\n(.*)\nSUMMARY OF ELECTORS',
		addition=None,
		correction=None,
		deletion=None,
	)

	box_patterns = dict(
		main=r'(\d+\nElectors(.*?(?=\n\d+\nElectors)|.*))',
		deletion=None
	)

	general_patterns = dict(
		state=r'STATE \([^()\n]+\) ([^\na-z]+)',
		acName=r'([^\n]+)(?=\n\d+\nELECTORAL ROLL)',
		partNo=r'^(\d+)',
		year=r'^\d+\n[^\n]+\n[^\n]+\n(\d+)',
		mainTown=r'([^\n]+)\n([^\n]+\n){3}(?=ELECTORAL ROLL)',
		mandal=r'([^\n]+)\n[^\n]+(?=\n\d{6}\n)',
		policeStation=r'([^\n]+)(\n[^\n]+){3}(?=\n\d{6}\n)',
		district=r'([^\n]+)(?=\n\d{6}\n)',
		stationName=r'(?<=\n\d{6}\n)[^\n]+\n([^\n]+)',
		stationAddress=r'(?<=\n\d{6}\n)[^\n]+\n[^\n]+\n(.+?)(?=\n\d+\n\d+)',
		netMale=r'Roll Identification :\n(\d+)',
		netFemale=r'Roll Identification :\n\d+\n(\d+)',
		netTotal=r'(\d+)(?=\nQualifying Date \(PR\))'
	)

	elector_patterns = dict(
		number=r'(\d+)(?=\nHouse No:)',
		name=r'(?<=Electors Name:)(.*)(?=Father|Husband|Mother)',
		relativeName=r'(?<=\'s Name:)(.*?)\n(?=Male|Female)',
		house=r'^(\d+)',
		age=r'(\d+)(?=\n[A-Z]{1,5}[0-9/]+)',
		sex=r'(Male|Female)'
	)


class JkPDF(Reader):

	pat = JkPatterns()

	def __init__(self, path):
		super(JkPDF, self).__init__(path)
