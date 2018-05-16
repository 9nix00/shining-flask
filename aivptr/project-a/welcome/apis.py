"""
=============

=============
"""

from flask import Blueprint

api = Blueprint('welcome', __name__)


@api.route('/')
def hello():
    return 'Welcome!'
