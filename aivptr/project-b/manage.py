"""
================
启动文件
================

该文件根据`Flask-Kickstart`方式生成

正确运行你需要当前项目能正确引用
`account`和`welcome` 组件
"""

import os
import sys

import click
from fantasy import create_app
from flask.cli import FlaskGroup

os.environ.setdefault('FANTASY_SETTINGS_MODULE', 'web.conf')
os.environ.setdefault('HIVE_APP', 'hello')

# hardcode
# 此处仅为演示方便，在真实开发中，应该避免这种策略
sys.path.insert(0, os.path.join(os.path.abspath(__file__).rsplit('/', 2)[0],
                                'project-a'))
sys.path.insert(0, os.path.dirname(__file__))

# 关闭一些高级特性
os.environ['FANTASY_ACTIVE_CACHE'] = 'no'
os.environ['FANTASY_ACTIVE_SENTRY'] = 'no'


# hardcode end


def app_tool(info):
    from flask_sqlalchemy import SQLAlchemy
    app = create_app(os.environ['HIVE_APP'], db=SQLAlchemy())
    return app


@click.group(cls=FlaskGroup, create_app=app_tool)
def cli():
    pass


cli()
