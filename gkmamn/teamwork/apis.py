from flask import Blueprint

api = Blueprint('teamwork', __name__)


@api.route('/')
def hello():
    return 'I am Teamwork.'
