from ..base import Reader, Patterns

__all__ = ['ManipurPDF']


class ManipurPatterns(Patterns):
    part_patterns = dict(
        main=r'Page3\n(.*)\nSUMMARY OF ELECTORS',
        addition=None,
        correction=None,
        deletion=None,
    )

    box_patterns = dict(
        main=r'(\d+\nName of Elector:(.*?(?=\n\d+\nName of Elector:)|.*))',
        deletion=None
    )

    general_patterns = dict(
        state=r'\nState : ([^\n]+)',
        acName=r'\nAssembly Constituency :\n([^\n]+)',
        pcName=r'Constituency is located :\n(.*?)(?=\nPart No. :)',
        partNo=r'\nPart No. : +(\d+)',
        year=r'Year of Revision :\n(\d+)',
        mainTown=r'([^\n]+)(?=\n\d+\n\d+\n\d+\n[^\n]+\nPanchayat :)',
        mandal=r'(?<=\n)([^0-9\n]+)\n[^\n]+(?=\n\d{6}\n)',
        policeStation=r'([^\n]+)\nPanchayat :\n',
        district=r'([^\n]+)\n\d{6}\n',
        stationName=r'\nTotal\n[\d/]+ -([^\n]+)',
        stationAddress=r'\n\d{6}\n(.+?)(?=(\n[^\n]+){8}\nPanchayat :)',
        netMale=r'\nPanchayat :\n(\d+)',
        netFemale=r'\nPanchayat :\n\d+\n(\d+)',
        netTotal=r'\nPanchayat :\n\d+\n\d+\n(\d+)'
    )

    elector_patterns = dict(
        number=r'^(\d+)',
        name=r'(?<=Sex:\n)(.+?)(?=\n(Female|Male)\n)',
        relativeName=r'(?<=[Mm]ale\n)(.+?)(?=\n\d+\n\d+\n[A-Z]{1,5}[0-9\/]+)',
        house=r'(?<=\n)(\d+)\n\d+\n[A-Z]{1,5}[0-9\/]+',
        age=r'(?<=\n)(\d+)\n[A-Z]{1,5}[0-9\/]+',
        sex=r'(Male|Female)'
    )


class ManipurPDF(Reader):
    pat = ManipurPatterns()

    def __init__(self, path):
        super(ManipurPDF, self).__init__(path)
