from flask import Blueprint

api = Blueprint('hello', __name__)


@api.route('/')
def hello():
    return 'Hello!'
