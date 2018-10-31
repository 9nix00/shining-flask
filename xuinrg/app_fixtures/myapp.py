"""
=============
基础依赖
=============
"""

import os

from pytest_fantasy.fixtures import (app, fantasy_celery_app, pytest_addoption,
                                     fantasy_cli)

_ = pytest_addoption
_ = fantasy_celery_app
_ = app
_ = fantasy_cli

os.environ.setdefault('FANTASY_MIGRATION_PATH',
                      os.path.join(__file__.rsplit('/', 2)[0]))

os.environ.setdefault('FANTASY_PRIMARY_NODE', 'yes')
os.environ['FANTASY_MIGRATION_PATH'] = __file__.rsplit('/', 2)[0]


def pytest_namespace():
    return {
        'resource_root': None,
        'app_entry': None,
        'active_db': 'yes',
        'active_cache': 'yes',
        'active_celery': os.environ.get('FANTASY_ACTIVE_CELERY') == 'yes',
        'app_config': {
            'SECRET_KEY': os.environ.get('FLASK_SECRET_KEY', 'HELLO,TEST'),
            'SQLALCHEMY_DATABASE_URI': os.environ.get(
                'SQLALCHEMY_DATABASE_URI',
                'mysql+pymysql://root:root@localhost/lego-test'),
            'SQLALCHEMY_TRACK_MODIFICATIONS': True,
            'CACHE_TYPE': 'redis',
            'CACHE_REDIS_URL': 'redis://localhost:6379/0',

            'FANTASY_PRIMARY_NODE': 'yes',
            'SECURITY_PASSWORD_SALT': 'Hi,Salt',
        },
        'entry_config': {}
    }
