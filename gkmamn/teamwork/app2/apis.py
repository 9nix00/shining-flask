from flask import Blueprint

api = Blueprint('teamwork.app2', __name__)


@api.route('/')
def hello():
    return 'I am app2!'
