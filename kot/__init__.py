from .core.kot import KOT
from .core.kot import console
from .core.kot import start_location, open_databases
from .core.kot import HASHES
from .core.serial import KOT_Serial

from .remote.remote import KOT_Remote
from .remote.interface import KOT_Cloud
from .remote.interface import KOT_Cloud_Pro
from .remote.interface import KOT_Cloud_Dedicated
from .remote.interface import KOT_Cloud_Dedicated_Prepare
from .remote.helper import no_exception
from .remote.helper import requires

__version__ = '0.42.0'


