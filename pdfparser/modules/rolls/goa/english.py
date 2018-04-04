from ..base import Reader, Patterns

__all__ = ['GoaPDF']


class GoaPatterns(Patterns):
    part_patterns = dict(
        main=r'(?<=Page3\n)(.*?)(?=\n\d+\. SUMMARY OF ELECTORS)',
        addition=None,
        correction=None,
        deletion=None,
    )

    box_patterns = dict(
        main=r'(EPIC NO:(.*?(?=EPIC NO:)|.*))',
        deletion=None
    )

    general_patterns = dict(
        state=r'(?<=State - )([^\n]+)',
        acName=r'Assembly Constituency : +([^\n]+)',
        pcName=r'Constituency is located : ([^\n]+)',
        partNo=r'(?<=Part No.) *(\d+)',
        year=r'(?<=Date Of Publication :\n)(\d+)',
        mainTown=r'(?<=PIN Code :\n)([^\n]+)',
        mandal=r'(?<=PIN Code :\n)[^\n]+\n[^\n]+\n([^\n]+)',
        policeStation=r'(?<=PIN Code :\n)[^\n]+\n([^\n]+)',
        district=r'([^\n]+)(?=\n\d{6}\n)',
        stationName=r'(?<=Name of Polling Station :\n)\d+\.(.+?)(?=Address of Polling Station)',
        stationAddress=r'(?<=Address of Polling Station :\n)(.+?)(?=Type of Polling Station)',
        netMale=r'(\d+)\n\d+\n\d+(?=\nMain Village)',
        netFemale=r'(\d+)\n\d+(?=\nMain Village)',
        netTotal=r'(\d+)(?=\nMain Village)'
    )

    elector_patterns = dict(
        number=r'(?<=\n)(\d+)(?=\n)',
        name=r'\n\d+\n(.+?)\n(?=Father|Husband|Mother)',
        relativeName=r'Sex: +[^\n]+\n(.+?)(?=\n\d+\n)',
        house=r'(?<=House No: )([^\n,]+)(?=,|\n)',
        age=r'Age: +(\d+)',
        sex=r'Sex: +([^\n]+)'
    )


class GoaPDF(Reader):
    pat = GoaPatterns()

    def __init__(self, path):
        super(GoaPDF, self).__init__(path)
