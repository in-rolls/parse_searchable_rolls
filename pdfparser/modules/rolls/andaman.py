from .base import Reader, Patterns

__all__ = ['AndamanPDF']


class AndamanPatterns(Patterns):
    box_patterns = dict(
        main=r'(\d*\n\d+\n(#\n)?Age :(.*?(?=\d+\n\d+\n(#\n)?Age :)|.*))',
        addition=r'([A-Z]{1,5}[0-9]+(.*?(?=\n[A-Z]{1,5}[0-9]+)|.*))',
        correction=r'([A-Z]{1,5}[0-9]+(.*?(?=\n[A-Z]{1,5}[0-9]+)|.*))',
    )

    general_patterns = dict(
        state=r'(?<=\n)([A-Z& ]+)(?= PARLIAMENTARY CONSTITUENCY)',
        pcName=r'\n(\d+ +- +[^a-z\n]+)\n',
        partNo=r'\n[\w ]+\n(\d+)\n(?=\d+-[\w() ]+)',
        year=r'(?<=PARLIAMENTARY CONSTITUENCY\n)(20\d{2})',
        mainTown=r'(?<=ELECTORAL ROLL -\n\d{6}\n)([^\n]+)',
        mandal=r'(?<=Panchyat :\n)[^\n]+\n\n?([^\n]+)',
        district=r'\d+-[\d\w ()]+\n([^a-z\n]+)(?=\n\d+ ?- ?)',
        stationName=r'\d+ +([^\n]+)(?=\nNil)',
        stationAddress=r'Other\n[\d\n]+([^\n]+)',
        netMale=r'Other\n\d+\n(\d+)',
        netFemale=r'Other\n\d+\n\d+\n(\d+)',
        netThird=r'Other\n\d+\n\d+\n\d+\n\d+\n\d+\n(\d+)',
        netTotal=r'Other\n\d+\n\d+\n\d+\n(\d+)'
    )

    elector_patterns = dict(
        number=r'(\d+)\n(?=Age :|[^\n]+\nName :)',
        name=r'(?<=Name :|Age :\n)([A-Z\s]+?)(?=Father|Husband|\d+)',
        relativeName=r'(?<=\'s Name :)([A-Z\s]+?(?=House No :|Males)|[A-Z\s]+)',
        house=[
            r'(?<=House No :)([0-9a-zA-Z /-]+)',
            r'([0-9a-zA-Z /-]+)(?=\n\d+\nSex :)'
        ],
        age=r'(\d+)\n(?=\d+\nAge :|Sex :)',
        sex=r'(?<=Sex :) ?(Male|Female|Other|Third Gender)'
    )


class AndamanPDF(Reader):
    pat = AndamanPatterns()

    def __init__(self, path):
        super(AndamanPDF, self).__init__(path)
