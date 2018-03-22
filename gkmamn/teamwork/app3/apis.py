from flask import Blueprint

api = Blueprint('teamwork.app3', __name__)


@api.route('/')
def hello():
    return 'I am app3!'
