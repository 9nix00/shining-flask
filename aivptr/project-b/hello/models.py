"""
=======================
账户实现
=======================

一个最简账户模块

"""

from flask import current_app

db = current_app.db


class Hello(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    pass
