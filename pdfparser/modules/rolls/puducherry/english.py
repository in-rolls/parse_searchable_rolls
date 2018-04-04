from ..base import Reader, Patterns

__all__ = ['PuducherryPDF']


class PuducherryPatterns(Patterns):
    part_patterns = dict(
        main=r'Page5\n(.*)\nSUMMARY OF ELECTORS',
        addition=None,
        correction=None,
        deletion=None
    )

    box_patterns = dict(
        main=r'([A-Z]{2,5}[/-]?[0-9]{2,}[A-Z0-9/-]*(.*?(?=[A-Z]{2,5}[/-]?[0-9]{2,}[A-Z0-9/-]*)|.*))',
        deletion=None
    )

    general_patterns = dict(
        state=r'ELECTORAL ROLL, \d+ \(U\d+\)([^\n]+)',
        acName=r'([^\n]+)\n\d+\n[^\n]+\nDistrict',
        pcName=r'([^\n]+)\n[^\n]+\n\d+\n[^\n]+\nDistrict',
        partNo=r'\n(\d+)\n[^\n]+\nDistrict',
        year=r'Date of Publication\n\n: ?(\d+)',
        mainTown=r'\nMain Village\n([^\n]+)',
        mandal=r'\nPincode\n([^\n]+)',
        policeStation=r'\nPincode\n[^\n]+\n([^\n]+)',
        district=r'\n\d+\n([^\n]+)\nDistrict\n',
        stationName=r'\n:\n[\d/]+ ?- ?([^:]*)(?=\n\d+\. NUMBER OF ELECTORS)',
        stationAddress=r'\nAddress of Polling\nStation\n:\n([^:]*)',
        netMale=r'\n(\d+)\n\d+\n\d+\n\d+$',
        netFemale=r'\n\d+\n(\d+)\n\d+\n\d+$',
        netThird=r'\n\d+\n\d+\n(\d+)\n\d+$',
        netTotal=r'\n\d+\n\d+\n\d+\n(\d+)$'
    )

    elector_patterns = dict(
        number=r'House No\.:[^\n]*\n(\d+)',
        name=r'\nName\n(.*?)\n(?=[Ff]ather|[Hh]usband|[Mm]other)',
        relativeName=r'(?<=\'s :\nName\n)(.*?)(?=\n:\n:\n)',
        house=r'House No\.:([^\n]*)\n',
        age=r'Age : ?(\d+)',
        sex=r'Sex ?:([^\n]*)\n'
    )


class PuducherryPDF(Reader):
    pat = PuducherryPatterns()
    general_pages = [1, 2]

    def __init__(self, path):
        super(PuducherryPDF, self).__init__(path)
