"""
=============
基础依赖
=============
"""

import os

import pytest


def pytest_namespace():
    return {
        'resource_root': None,
        'app_entry': None,
        'active_db': os.environ.get('FANTASY_ACTIVE_DB') == 'yes',
        'active_cache': os.environ.get('FANTASY_ACTIVE_CACHE') == 'yes',
        'active_celery': os.environ.get('FANTASY_ACTIVE_CELERY') == 'yes',
        'app_config': {
            'SECRET_KEY': os.environ.get('FLASK_SECRET_KEY', 'HELLO,TEST'),
        },
        'entry_config': {}
    }


def pytest_addoption(parser):
    parser.addoption("--keep-database", action="store_true",
                     default=False,
                     help="操作完成不清理数据库")
    pass


@pytest.fixture
def app(request):
    if not pytest.entry_app:
        raise KeyError("Please set `entry_app` namespace.")

    app_config = {key: getattr(pytest.app_config,
                               key) for key in dir(pytest.app_config)
                  if not key.startswith('_')}

    if hasattr(pytest, 'entry_config'):
        temp_config = {key: getattr(pytest.entry_config,
                                    key) for key in dir(pytest.entry_config)
                       if not key.startswith('_')}

        entry_config = {}
        for key, value in temp_config.items():
            if hasattr(value,
                       '__name__') and \
                    value.__name__.split('.', 1)[0] == 'pytest':
                entry_config[key] = {k: getattr(value,
                                                k) for k in dir(value)
                                     if not k.startswith('_')}
            else:
                entry_config[key] = value
            pass

        app_config.update(entry_config)

    from fantasy import create_app

    db = None
    if pytest.active_db:
        from flask_sqlalchemy import SQLAlchemy
        db = SQLAlchemy()
        pass

    celery = None
    if pytest.active_celery:
        from celery import Celery
        celery = Celery(pytest.entry_app)
        pass

    app = create_app(pytest.entry_app, app_config, db, celery)

    yield app

    if pytest.active_db:
        from sqlalchemy.engine.url import make_url
        from sqlalchemy_utils import drop_database
        drop_database(make_url(app_config['SQLALCHEMY_DATABASE_URI']))

    mongodb_config = app.config.get('MONGODB_SETTINGS')

    if mongodb_config:
        try:
            from mongoengine.connection import get_db
            current_mongodb = get_db()
            current_mongodb.client.drop_database(mongodb_config['DB'])
        except Exception as e:
            print("drop mongodb ignored", e)
            pass

    if hasattr(pytest, 'entry_tear_down'):
        func = getattr(pytest, 'entry_tear_down')
        func(app)
        pass

    pass


@pytest.fixture
def fantasy_celery_app(client):
    app = client.application
    celery_app = app.celery
    celery_app.conf.update(CELERY_ALWAYS_EAGER=True)
    return celery_app
