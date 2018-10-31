"""
=============
测试用例
=============

"""

from flask import url_for


# def test_register_no_allow(client):
#     response = client.get(url_for('accounts.username.register'))
#     assert 405 == response.status_code
#     pass
#
#
# def test_register_no_input(client):
#     response = client.post(url_for('accounts.username.register'))
#
#     assert 422 == response.status_code
#     assert True == ('errors' in response.json)
#     pass


# def test_register_no_password(client):
#     response = client.post(url_for('accounts.username.register'), data={
#         'username': 'abc',
#     })
#
#     assert 422 == response.status_code
#     assert True == ('errors' in response.json)
#     assert True == ('password' in response.json['errors'])
#     pass


# def test_register_no_user(client):
#     response = client.post(url_for('accounts.username.register'), data={
#         'password': 'abcKalskakxlalq10290ak',
#     })
#
#     assert 422 == response.status_code
#     assert True == ('errors' in response.json)
#     assert True == ('username' in response.json['errors'])
#     pass


# def test_register_too_short(client):
#     response = client.post(url_for('accounts.username.register'), data={
#         'username': 'h',
#         'password': 'a',
#     })
#
#     assert 422 == response.status_code
#     assert True == ('errors' in response.json)
#     assert True == ('username' in response.json['errors'])
#     assert True == ('password' in response.json['errors'])
#     pass
#
#
# def test_register_too_long(client):
#     response = client.post(url_for('accounts.username.register'), data={
#         'username': 'h' * 31,
#         'password': 'a' * 33,
#     })
#
#     assert 422 == response.status_code
#     assert True == ('errors' in response.json)
#     assert True == ('username' in response.json['errors'])
#     pass
#
#
# def test_register_invalid_start(client):
#     response = client.post(url_for('accounts.username.register'), data={
#         'username': '_' * 10,
#         'password': 'a' * 16,
#     })
#     assert 422 == response.status_code
#     assert True == ('errors' in response.json)
#     assert True == ('username' in response.json['errors'])
#
#     response = client.post(url_for('accounts.username.register'), data={
#         'username': '0' * 10,
#         'password': 'a' * 16,
#     })
#     assert 422 == response.status_code
#     assert True == ('errors' in response.json)
#     assert True == ('username' in response.json['errors'])
#     pass
#
#
# def test_register_ok(client):
#     response = client.post(url_for('accounts.username.register'), data={
#         'username': 'hello-world',
#         'password': 'abcKalskakxlalq10290ak'
#     })
#
#     assert 201 == response.status_code, response.status_code
#
#     assert True == ('id' in response.json), response.json
#     assert True == ('active' in response.json), response.json
#     assert True == ('username' in response.json), response.json
#     pass
#
#
# def test_register_disable(client):
#     client.application.config['ACCOUNT_USERNAME_DISABLE_REGISTER'] = True
#
#     response = client.post(url_for('accounts.username.register'), data={
#         'username': 'hello-world',
#         'password': 'abcKalskakxlalq10290ak'
#     })
#
#     assert 422 == response.status_code, response.status_code
#
#     assert True == ('errors' in response.json), response.json
#     assert True == ('global' in response.json['errors']), response.json[
#         'errors']
#     pass
#
#
# def test_login_invalid(client):
#     response = client.post(url_for('accounts.username.login'), data={})
#
#     assert 422 == response.status_code, response.status_code
#
#     assert True == ('errors' in response.json), response.json
#     assert True == ('username' in response.json['errors']), response.json[
#         'errors']
#     assert True == ('password' in response.json['errors']), response.json[
#         'errors']
#     pass
#
#
# def test_login_no_user(client):
#     response = client.post(url_for('accounts.username.login'), data={
#         'username': 'hello-world',
#         'password': 'aaaassss'
#     })
#
#     assert 422 == response.status_code, response.status_code
#
#     assert True == ('errors' in response.json), response.json
#     assert True == ('username' in response.json['errors']), response.json[
#         'errors']
#     assert False == ('password' in response.json['errors']), response.json[
#         'errors']
#     pass
#
#
# def test_login_wrong_password(client, fixture_register):
#     response = client.post(url_for('accounts.username.login'), data={
#         'username': 'ciuser',
#         'password': 'wrong'
#     })
#
#     assert 422 == response.status_code, response.status_code
#     assert True == ('errors' in response.json), response.json
#     assert False == ('username' in response.json['errors']), response.json[
#         'errors']
#     assert True == ('password' in response.json['errors']), response.json[
#         'errors']
#     pass


def test_login_ok(client, fixture_register):
    response = client.post(url_for('accounts.username.login'), data={
        'username': 'ciuser',
        'password': 'cipassword'
    })

    assert 200 == response.status_code, response.status_code
    assert True == ('id' in response.json), response.json
    assert True == ('token' in response.json), response.json

    from flask_security.core import _get_serializer
    from account.models import Account

    s = _get_serializer(client.application, 'remember')
    uid, password = s.loads(response.json['token'])

    account = Account.query.get(uid)
    assert int(uid) == int(account.id)
    pass
