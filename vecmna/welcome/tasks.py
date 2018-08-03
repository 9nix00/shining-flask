"""
=============

=============
"""

from flask import current_app as app

celery = app.celery


@celery.task
def hello_world(a, b):
    print("hello world: %d+%d" % (a, b))
    return True
