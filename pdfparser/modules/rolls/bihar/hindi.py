from ..base import Reader, Patterns

__all__ = ['BiharPDF']


class BiharPatterns(Patterns):
    part_patterns = dict(
        main=r'Page2(.*?)(?=Summary of Electors)',
        addition=None,
        correction=None,
        deletion=None,
    )

    box_patterns = dict(
        main=r'(?<=\n)(Name :(.*?(?=\nName :)|.*))',
        deletion=None
    )

    general_patterns = dict(
        state=r'[A-Z]+[0-9]+ - ([^\n]+)(?=\n)',
        acName=r'\n(\d+ *- *[^a-z\n]+)\n',
        pcName=r'\n(\d+ *, *[^\n]+)\n',
        partNo=r'Net Electors\n\d+\n(\d+)',
        year=r'Year of Revision\n: (\d+)',
        mainTown=r'[A-Z]+[0-9]+ - [^\n]+\n([^\na-z]+)',
        policeStation=r'[A-Z]+[0-9]+ - [^\n]+\n[^\n]+\n[^\n]+\n([^\n]+)',
        mandal=r'(?<=\n)([^\n]+)(?=\n\d{6}\n)',
        district=r'\n\d+\.[^a-z]+\n([A-Z ]+)\n',
        stationName=r'\d+ +([^\na-z]+)(?=\n[A-Z]+[0-9]+ - [^\n]+\n)',
        stationAddress=r'\n\d+\.[^\na-z]+\n[^\na-z]+\n([^a-z]+)(?=\n[^\n]+\n\d+)',
        netMale=r'(?<=\n\d{6}\n)(\d+)',
        netFemale=r'(?<=\n\d{6}\n)\d+\n(\d+)',
        netThird=r'(?<=\n\d{6}\n)\d+\n\d+\n(\d+)',
        netTotal=r'(?<=\n\d{6}\n)\d+\n\d+\n\d+\n(\d+)'
    )

    elector_patterns = dict(
        number=r'(?<=\n)(\d+)\n(?=Husband|Father|Mother)',
        name=r'(?<=^Name :)([^\n]*)(?=\n)',
        relativeName=r'(?<=\'s Name :)([^\na-z]*)(?=\n)',
        house=r'(?<=House No :)([^\n]*)(?=\n)',
        age=r'(?<=age :) *(\d+)(?=\n)',
        sex=r'(?<=Gender :)([^\n]+)(?=\n)'
    )


class BiharPDF(Reader):
    pat = BiharPatterns()

    def __init__(self, path):
        super(BiharPDF, self).__init__(path)
