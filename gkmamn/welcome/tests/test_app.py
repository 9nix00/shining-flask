"""
=============

=============
"""

from flask import url_for


def test_hello(client):
    response = client.get(url_for('welcome.hello'))
    assert 200 == response.status_code
    pass
