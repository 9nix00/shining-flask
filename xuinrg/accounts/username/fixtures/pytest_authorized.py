"""
=================
测试组件共享用例
=================
"""

import pytest


@pytest.fixture(scope='function')
def fixture_register(request):
    from accounts.username.utils import register
    from sqlalchemy.exc import IntegrityError
    try:
        register('ciuser', 'cipassword')
    except IntegrityError:
        pass

    from accounts.username.models import AccountUsername
    username = AccountUsername.query.filter_by(username='ciuser').first()
    return username


@pytest.fixture(scope='function')
def fixture_login(request, fixture_register):
    from accounts.username.utils import login
    result = login('ciuser', 'cipassword')
    return {
        'Authentication-Token': result['token']
    }
    pass
