try:
    from .architecture import *
except ImportError:
    pass
try:
    from .dependency_detector import *
except ImportError:
    pass
try:
    from .framework_detector import *
except ImportError:
    pass
try:
    from .repository import *
except ImportError:
    pass
