"""
================
CLI启动文件
================

该文件根据`Flask-Kickstart`方式生成

正确运行你需要当前项目能正确引用
`account`和`welcome` 组件


.. note::

    引用方式务必按照 from xxx.app import app as xxxx
    的格式，我们的db处理工具，需要依赖完全正确的格式匹配



"""

import os

import click
from fantasy import create_app, create_celery
from flask.cli import FlaskGroup

os.environ.setdefault('FANTASY_SETTINGS_MODULE', 'web.conf')
os.environ.setdefault('HIVE_APP', 'welcome')
os.environ.setdefault('CELERY_BROKER_URL', 'redis://127.0.0.1:6379/1')
os.environ.setdefault('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379/2')


def app_tool(info):
    from flask_sqlalchemy import SQLAlchemy

    celery = create_celery(
        os.environ.get('CELERY_APP_NAME', 'fantasy'))

    app = create_app(os.environ['HIVE_APP'], db=SQLAlchemy(), celery=celery)
    return app


@click.group(cls=FlaskGroup, create_app=app_tool)
def cli():
    pass


cli()
