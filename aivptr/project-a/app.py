"""
=============
代理层
=============
"""

import os
# hardcode
# 此处仅为演示方便，在真实开发中，应该避免这种策略
import sys

from flask_sqlalchemy import SQLAlchemy

sys.path.insert(0, os.path.dirname(__file__))

os.environ['FANTASY_PRIMARY_NODE'] = 'yes'
# 关闭一些高级特性
os.environ['FANTASY_ACTIVE_CACHE'] = 'no'
os.environ['FANTASY_ACTIVE_SENTRY'] = 'no'
# hardcode end

from fantasy import create_app
from werkzeug.wsgi import DispatcherMiddleware

db = SQLAlchemy()

os.environ.setdefault('FANTASY_SETTINGS_MODULE', 'web.conf')


app = DispatcherMiddleware(create_app('welcome', db=db))

if __name__ == '__main__':
    import os
    from werkzeug.serving import run_simple

    bind_ip = os.environ.get('FLASK_SIMPLE_BIND', '127.0.0.1')

    run_simple(bind_ip, 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)
