"""
=======================
账户实现
=======================

一个最简账户模块

"""

from flask import current_app
from flask_security import UserMixin, RoleMixin

db = current_app.db

roles_users = db.Table(
    'roles_users',
    db.Column('account_id', db.Integer(), db.ForeignKey('account.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Account(db.Model, UserMixin):
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
