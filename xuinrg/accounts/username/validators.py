"""
=============
验证器
=============

"""

from webargs.core import ValidationError

from .models import AccountUsername


def username_exists(val):
    if AccountUsername.query.filter_by(username=val).first():
        raise ValidationError('用户名已注册', status_code=422)
    pass
