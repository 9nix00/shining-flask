"""
=============
API
=============

"""

from flask import Blueprint, current_app as app, jsonify
from webargs import fields, validate
from webargs.flaskparser import use_args, abort

# from flask_security.decorators import anonymous_user_required

from guard.ip import ratelimit
from . import validators, utils

api = Blueprint('accounts.username', __name__)
db = app.db


@ratelimit(limit=10, interval=300, key_prefix='register')
@api.route('/register.api', methods=['post'])
# @anonymous_user_required
@use_args({
    'username': fields.Str(required=True, validate=[
        validate.Length(min=6, max=30),
        validate.Regexp('^[a-zA-Z][a-zA-Z0-9_\-]+'),
        validators.username_exists
    ]),
    'password': fields.Str(required=True, validate=validate.Length(min=8,
                                                                   max=32)),
}, locations=('form', 'json'))
def register(args):
    if app.config.get('ACCOUNT_USERNAME_DISABLE_REGISTER', True):
        abort(422, errors={
            'global': '网站禁止使用用户名方式注册'
        })

    return jsonify(utils.register(args['username'],
                                  args['password'])), 201


@ratelimit(limit=5, interval=300, key_prefix='login:username')
@api.route('/login.api', methods=['post'])
# @anonymous_user_required
@use_args({
    'username': fields.Str(required=True),
    'password': fields.Str(required=True),
}, locations=('form', 'json'))
def login(args):
    try:
        data = utils.login(args['username'],
                           args['password'])
    except ValueError as e:
        abort(422, errors={
            e.args[i]: e.args[i + 1] for i in range(0, len(e.args), 2)
        })
    else:
        return jsonify(data), 200

    pass
