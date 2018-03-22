"""
=============

=============
"""

import sys

sys.path.insert(0, __file__.rsplit('/', 3)[0])
pytest_plugins = "fantasy.fixtures.pytest_hive",


def pytest_namespace():
    return {
        'entry_app': 'welcome'
    }
