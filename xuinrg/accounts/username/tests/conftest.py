"""
=============

=============
"""

import os

pytest_plugins = ("app_fixtures.myapp",
                  "accounts.username.fixtures.pytest_authorized")


def pytest_namespace():
    return {
        'resource_root': os.path.join(os.path.dirname(__file__),
                                      'test-resources'),
        'entry_app': 'accounts.username',
        'entry_config': {}
    }
