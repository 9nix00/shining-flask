"""
=============
代理层
=============
"""

import os

# hardcode
# 此处仅为演示方便，在真实开发中，应该避免这种策略
import sys

sys.path.insert(0, os.path.dirname(__file__))

# 关闭一些高级特性
os.environ['FANTASY_ACTIVE_DB'] = 'no'
os.environ['FANTASY_ACTIVE_CACHE'] = 'no'
os.environ['FANTASY_ACTIVE_SENTRY'] = 'no'
os.environ['FANTASY_ACTIVE_ACCOUNT'] = 'no'
# hardcode end

from fantasy import create_app
from werkzeug.wsgi import DispatcherMiddleware

os.environ.setdefault('FANTASY_SETTINGS_MODULE', 'web.conf')

app = DispatcherMiddleware(create_app('welcome'), {
    '/hello': create_app('hello'),
    '/teamwork/app3': create_app('teamwork.app3'),
    '/teamwork/app2/01': create_app('teamwork.app2.app1'),
    '/teamwork/app2': create_app('teamwork.app2'),
    '/teamwork/app1': create_app('teamwork.app1'),
    '/teamwork': create_app('teamwork'),
})

if __name__ == '__main__':
    import os
    from werkzeug.serving import run_simple

    bind_ip = os.environ.get('FLASK_SIMPLE_BIND', '127.0.0.1')

    run_simple(bind_ip, 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)
