import warnings

from .clientturtle import ClientTurtle
from .serverturtle import Server, get_server_socket

try:
    import gpiozero
    from .roboturtle import RoboTurtle
except ImportError:
    warnings.warn("Package 'gpiozero' not found (this is for raspberry Pi only).  LocalTurtle will not work")