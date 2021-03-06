"""Package for mctweetyface."""

import sys

__project__ = 'mctweetyface'
__version__ = '0.0.0'

VERSION = "{0} v{1}".format(__project__, __version__)

PYTHON_VERSION = 3, 5

if sys.version_info < PYTHON_VERSION:  # pragma: no cover (manual test)
    sys.exit("Python {}.{}+ is required.".format(*PYTHON_VERSION))
