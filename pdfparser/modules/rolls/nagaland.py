from .base import Reader, Patterns, Elector

__all__ = ['NagalandPDF']


class NagalandPatterns(Patterns):

	part_patterns = dict(
		main=r'Page3\n(.*)\nSUMMARY OF ELECTORS',
		addition=r'List I : New Additions(.*)List II : Deletions',
		correction=r'List III : Modifications(.*)',
		deletion=r'List II : Deletions(.*)List III : Modifications',
	)

	box_patterns = dict(
		main=r'(\d+\nHouse No :(.*?(?=\n\d+\nHouse No :)|.*))',
		addition=r'([\dA-Za-z -/]*\n[A-Z ]+\n\d+\nN(.*?(?=\n[\dA-Za-z -/]*\n[A-Z ]+\n\d+\nN)|.*))',
		correction=r'(\d+\n[A-Z ]+\n\d+\nM(.*?(?=\n\d+\n[A-Z ]+\n\d+\nM)|.*))'
	)

	general_patterns = dict(
		state=r'S\d+ - ([^\n]+)',
		acName=r'(?<=\n)\d+ - [A-Z- &]+( \([\w ]+\))?(?=\n)',
		partNo=r'Net Electors\n\d+\n(\d+)',
		year=r'Year of Revision\d?\n: (\d+)',
		mainTown=r'([^\n]+)\n[^\n]+\n[^\n]+(?=\n\d{6}$)',
		mandal=r'([^\n]+)(?=\n\d{6}$)',
		policeStation=r'([^\n]+)\n[^\n]+(?=\n\d{6}$)',
		district=r'\n([A-Z@:/._+, -]+)\n([^a-z]+\n)*(?=\w+\n\d+\n)',
		stationName=r'\d+ +([A-Z ]+)(?=\n[A-Z]\d+ - [\w ]+\n)',
		stationAddress=r'\n[A-Z@:/._+, -]+\n([^a-z]+\n)*(?=\w+\n\d+\n)',
		netMale=r'\n\d+\n(\d+)\n\d+\n\d+\n\d+\n',
		netFemale=r'\n\d+\n\d+\n(\d+)\n\d+\n\d+\n',
		netThird=r'\n\d+\n\d+\n\d+\n(\d+)\n\d+\n',
		netTotal=r'\n\d+\n\d+\n\d+\n\d+\n(\d+)\n'
	)

	elector_patterns = dict(
		number={
			'main': r'^(\d+)',
			'*': r'(?<=\n[NM]\n)(\d+)',
		},
		name={
			'main': r'Name : (.+?)\n(?=Father|Husband|Mother)',
			'*': r'(?<=\'s\nName :\n)([^\n]+)'
		},
		relativeName={
			'main': r'(?<=\'s Name : )(.+?)\n\d+(?=$|\n)',
			'*': [
				r'(?<=\n)([^\n]+)\n\d+(?=\n[NM]\n)',
				r'(?<=\'s\nName :\n)[^\n]+(\n[A-Z .-]+?(?=$|\n))*'
			]
		},
		house={
			'main': r'House No : ([^\n]+)',
			'*': r'^(\d+)(?=\n[A-Z .-]+\n)'
		},
		age={
			'main': r'(?<=\'s Name : )[^\n]+\n(\d+)(?=$|\n)',
			'*': r'(\d+)(?=\n[NM]\n)'
		},
		sex={
			'main': r'Gender : ([^\n]+)',
			'*': r'[A-Z]{1,5}[0-9\/]+\n([^\n]+)'
		}
	)


class NagalandElector(Elector):

	merged_patterns = True


class NagalandPDF(Reader):

	pat = NagalandPatterns()

	def __init__(self, path):
		super(NagalandPDF, self).__init__(path, cls_elector=NagalandElector)
