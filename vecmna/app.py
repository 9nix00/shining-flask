"""
========================
最小化启动
========================

该文件根据`Flask-Kickstart`方式生成

最小化启动相当于flask的quick start,
不依赖于任何IO服务。

"""
import os

import sys  # 此行仅为了演示方便

sys.path.insert(0, __file__.rsplit('/', 2)[0])  # 此行仅为了演示方便

from fantasy import create_app                       # noqa: E402
from werkzeug.wsgi import DispatcherMiddleware       # noqa: E402

os.environ.setdefault('HIVE_APP', 'welcome')  # 此行仅为了演示方便
os.environ.setdefault('FANTASY_SETTINGS_MODULE', 'web.conf')  # 此行仅为了演示方便

app = DispatcherMiddleware(create_app('welcome'))

if __name__ == '__main__':
    import os
    from werkzeug.serving import run_simple

    bind_ip = os.environ.get('FLASK_SIMPLE_BIND', '0.0.0.0')

    run_simple(bind_ip, 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)
