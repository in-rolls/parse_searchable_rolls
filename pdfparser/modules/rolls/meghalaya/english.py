from ..base import Reader, Patterns

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
        state=r'(?<=\n)S\d+ *- *([^\n]+)',
        acName=r'\n\d+\n(\d+ ?- ?[^a-z\n]+(\s*\([\w ]+\))?)\n',
        pcName=r'\n(\d+ *- *[^a-z\n()]+ +\([^a-z\n()]+\))\n',
        partNo=r'Net Electors\n\d+\n(\d+)',
        year=r'Year of Revision\n: (\d+)',
        mainTown=r'\n\d{6}\n[^\n]+\n(.*?)(?=\n[^\n]+\nPostOffice\n)',
        mandal=None,
        policeStation=r'\n\d{6}\n([^\n]+)',
        district=r'Net Electors.*?(?<=\n)([A-Z ]{4,})(?=\n)',
        stationName=r'\n\d+ +([^\n]+)(?=\n[A-Z]\d+ - [^\n]+)',
        stationAddress=r'\n\d+\.[A-Z ]+\n(?!\d+\.[A-Z ]+).*?(?<=\n)[A-Z ]{4,}(?=\n)(.*?)(?=\n[^\n]+\n\d+\n)',
        netMale=r'(\d+)\n\d+\n\d+\n\d+(?=\n(\d{6}|XXXX)\n)',
        netFemale=r'(\d+)\n\d+\n\d+(?=\n(\d{6}|XXXX)\n)',
        netThird=r'(\d+)\n\d+(?=\n(\d{6}|XXXX)\n)',
        netTotal=r'(\d+)(?=\n(\d{6}|XXXX)\n)'
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
