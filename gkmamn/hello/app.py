"""
=============
独立运行实例
=============

请确认端口8000未占用
"""

import sys

sys.path.insert(0, __file__.rsplit('/', 2)[0])

from flask import Flask
from hello import run_app

app = Flask(__name__)
run_app(app)
app.run(port=8000)
