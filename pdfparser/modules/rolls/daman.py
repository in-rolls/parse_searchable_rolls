from .base import Reader, Patterns, Elector

__all__ = ['DamanPDF']


class DamanPatterns(Patterns):
    part_patterns = dict(
        main=r'(?<=Page2)(.*?)(?=\nSUMMARY OF ELECTORS\n)',
        addition=None,
        correction=None,
        deletion=None,
    )

    box_patterns = dict(
        main=r'(\d+\n[FHM]\. Name :(.*?(?=\n\d+\n[FHM]\. Name :)|.*))',
        deletion=None
    )

    general_patterns = dict(
        state=r'(?<=Photo Electoral Roll - \d{4}, )([^\n]+)',
        acName=r'([^\n]+)$',
        partNo=r'^[^\n]+\n(\d+)',
        year=r'Year of Revision +: (\d+)',
        mainTown=r'(?<=Main Village Town\n:\n)([^\na-z]+)',
        policeStation=r'([^\na-z]+)(?=\n\d{6}\n)',
        district=r'(?<=Main Village Town\n:\n)[^\n]+\n([^\na-z]+)',
        stationName=r'\d+ ,.*,([^a-z]+)(?=\n\d+\nPhoto Electoral)',
        stationAddress=r'\d+ ,(.*)(?=\n\d+\nPhoto Electoral)',
        netMale=r'^[^\n]+\n\d+\n\d+\n(\d+)',
        netFemale=r'^[^\n]+\n\d+\n\d+\n\d+\n(\d+)',
        netThird=r'^[^\n]+\n\d+\n\d+\n\d+\n\d+\n\d+\n\d+\n(\d+)',
        netTotal=r'^[^\n]+\n\d+\n\d+\n\d+\n\d+\n(\d+)'
    )

    elector_patterns = dict(
        number=r'^(\d+)',
        name=r'(?<=Name :- )([^\n]+)',
        relativeName=r'(?<=Name :- )[^\n]+\n(.*?)(?=$|\n)',
        house=r'(?<=[FHM]\. Name :\n)[^\n]+\n([^\n]+)(?=\n[A-Z]{1,5}[0-9\/]+)',
        age=r'(?<=Age:\n)(\d+)',
        sex=r'(?<=[FHM]\. Name :\n)([^\n]+)(?=\n)',
        relativeType=r'(?<=\n)([FHM])(?=\. Name :)'
    )


class DamanElector(Elector):
    husband = 'H'


class DamanPDF(Reader):
    pat = DamanPatterns()

    def __init__(self, path):
        super(DamanPDF, self).__init__(path, cls_elector=DamanElector)
