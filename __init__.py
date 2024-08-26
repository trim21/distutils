__requires__ = [
    "jaraco.envs>=2.4; extra == 'test'",
    "jaraco.path; extra == 'test'",
    "jaraco.text; extra == 'test'",
    "path >= 10.6; extra == 'test'",
    "docutils; extra == 'test'",
    "pyfakefs; extra == 'test'",
    "more_itertools; extra == 'test'",
]

import importlib
import sys

__version__, _, _ = sys.version.partition(' ')


try:
    # Allow Debian and pkgsrc (only) to customize system
    # behavior. Ref pypa/distutils#2 and pypa/distutils#16.
    # This hook is deprecated and no other environments
    # should use it.
    importlib.import_module('_distutils_system_mod')
except ImportError:
    pass
