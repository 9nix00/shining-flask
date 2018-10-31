"""
=============
常用函数集
=============

"""

from uuid import uuid1

from flask import current_app as app
from flask_login import login_user
from flask_login import logout_user
from flask_principal import AnonymousIdentity, identity_changed
from flask_security.utils import hash_password, verify_password

from account.models import Account
from . import models

db = app.db


def register(username, password):
    code = uuid1()

    hashed_password = hash_password(password + code.hex)

    account = Account(
        active=True,
        password=hashed_password,
        code=code
    )

    user = models.AccountUsername(
        username=username,
        account=account
    )

    db.session.add(account)
    db.session.add(user)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        pass

    return {
        'id': account.id,
        'active': account.active,
        'username': user.username
    }


def login(username, password):
    user = models.AccountUsername.query.filter_by(
        username=username).first()

    if not user:
        raise ValueError('username', '无效的用户名')

    account = user.account
    if account.active is False:
        raise ValueError('active', '该账户已被禁用')

    if verify_password(password + account.code.hex, account.password) is False:
        raise ValueError('password', '密码错误')

    login_user(account, remember=False)  # 必须要执行此步，设置全局的current_user

    return {
        'id': account.id,
        'token': account.get_auth_token()
    }
    pass


def logout():
    identity_changed.send(app._get_current_object(),
                          identity=AnonymousIdentity())

    logout_user()
    pass
