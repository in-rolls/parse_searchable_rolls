import sys
from .errors import RollParseError
from . import andaman
from . import andhra
from . import arunachal
from . import dadra
from . import daman
from . import goa
from . import jk
from . import manipur
from . import meghalaya
from . import mizoram
from . import nagaland
from . import puducherry

__all__ = [
    'RollParseError',
    'andaman',
    'andhra',
    'arunachal',
    'dadra',
    'daman',
    'goa',
    'jk',
    'manipur',
    'meghalaya',
    'mizoram',
    'nagaland',
    'puducherry'
]

states = {s: getattr(sys.modules[__name__], s).__all__ for s in __all__ if not s.endswith('Error')}
