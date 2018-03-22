"""
=======================
账户实现
=======================

本章不讨论账户部分的实现。

..note::
    此处只为了配合测试用例正常运行,仅作最小化实现。
    请不要直接使用该代码。

    后续我们会在公众号其他文章中讨论账户部分的实现

"""

from flask import current_app
from flask_security import UserMixin, RoleMixin

db = current_app.db


roles_users = db.Table(
    'roles_users',
    db.Column('account_id', db.Integer(), db.ForeignKey('account.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Account(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('account', lazy='dynamic'))
    pass


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name
