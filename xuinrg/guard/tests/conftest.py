"""
=============

=============
"""

pytest_plugins = (
    "app_fixtures.myapp",
    "accounts.username.fixtures.pytest_authorized",)


def pytest_namespace():
    return {
        'entry_app': 'guard'
    }
