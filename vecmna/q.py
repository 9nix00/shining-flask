"""
================
Queue启动文件
================

该文件根据`Flask-Kickstart`方式生成

正确运行你需要当前项目能正确引用
`account`和`welcome` 组件


.. note::

    引用方式务必按照 from xxx.app import app as xxxx
    的格式，我们的db处理工具，需要依赖完全正确的格式匹配



"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, __file__.rsplit('/', 1)[0])

from fantasy import create_app, create_celery, load_tasks   # noqa: E402
from flask_sqlalchemy import SQLAlchemy                     # noqa: E402

os.environ.setdefault('FANTASY_SETTINGS_MODULE', 'web.conf')
os.environ.setdefault('HIVE_APP', 'welcome')
os.environ.setdefault('CELERY_BROKER_URL', 'redis://127.0.0.1:6379/1')
os.environ.setdefault('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379/2')

mod = os.environ['HIVE_APP']
celery = create_celery(
    os.environ.get('CELERY_APP_NAME', 'fantasy'))

app = create_app(mod, db=SQLAlchemy(), celery=celery)
load_tasks(app, __file__)
