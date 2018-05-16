"""
=============
配置文件
=============
"""

import os

DEBUG = True if os.environ.get('FLASK_DEBUG', 'no') == 'yes' else False
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    'mysql+pymysql://root:hello_world@127.0.0.1:3306/project_b')

SQLALCHEMY_TRACK_MODIFICATIONS = True if os.environ.get(
    'SQLALCHEMY_TRACK_MODIFICATIONS', 'yes') == 'yes' else False
