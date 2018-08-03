"""
=============

=============
"""

from flask import Blueprint, jsonify

api = Blueprint('welcome', __name__)


@api.route('/')
def hello():
    return jsonify({
        'hello': 'world'
    })


@api.route('/hello-celery.api')
def queue():
    from .tasks import hello_world
    hello_world.delay(1, 1)
    return jsonify({'status': 'send'})
