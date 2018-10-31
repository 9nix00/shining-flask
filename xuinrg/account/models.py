"""
=============
Models
=============
"""

from flask import current_app
from flask_security import UserMixin, RoleMixin
from sqlalchemy.sql.expression import text
from sqlalchemy_utils import UUIDType

db = current_app.db

roles_users = db.Table(
    'roles_users',
    db.Column('account_id', db.Integer(), db.ForeignKey('account.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Account(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(128), nullable=False)
    code = db.Column(UUIDType(),
                     doc='随机码，用于密码校验，提升安全性',
                     nullable=False)

    active = db.Column(db.Boolean, default=True,
                       doc='只有激活状态的用户才能正常使用本站',
                       nullable=False)

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('account', lazy='dynamic'))

    date_joined = db.Column(db.DateTime, server_default=text('NOW()'),
                            nullable=False)

    pass


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name
