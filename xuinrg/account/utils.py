"""
=============
基础操作
=============

以下部分代码来自于 flask-security

Flask-Security整体很符合我们的预期，但是form部分我们不喜欢。
另外一个原因是 Flask-Security 其实本身也是基于 Flask-Login的。

出于学习和更好用的目的，我们整理代码并构造自己的。

我们需要构造一个可以兼容Flask-Security的版本

"""


from flask_security.passwordless import login_token_status

from .models import Account


def authorized(token):
    expired, invalid, account_id = login_token_status(token)

    if expired:
        raise ValueError('expired', '认证已过期，请重新登录')

    if invalid:
        raise ValueError('invalid', '无效的认证信息，请重新登录')

    account = Account.query.get(account_id)
    return account


