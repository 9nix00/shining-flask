"""
=============
创建账户工具
=============
"""

from getpass import getpass

import click
from flask.cli import with_appcontext

from accounts.username.utils import register, login


@click.group()
def user():
    """
    账户工具
    """
    pass


class Env:
    app_id = None
    app_key = None
    agent = 'Tool-Box 1.0'

    api_download = 'https://www.yunaq.com' + '/api/v3/log_download'
    api_site_query = 'https://www.yunaq.com' + '/api/v3/site'
    pass


@user.command('initial')
@click.argument('username')
@click.option('--password', envvar='ACCOUNT_USER_PASSWORD')
@click.option('--is-admin', is_flag=True, help='TODO feature')
@click.option('--is-bot', is_flag=True, help='TODO feature')
@with_appcontext
def initial(username, password, is_admin, is_bot):
    """
    创建用户

    创建用户要求可以直连到数据库
    """
    password = password or getpass('please input your password:')
    register(username, password)
    pass


@user.command('token')
@click.argument('username')
@click.option('--password', envvar='ACCOUNT_USER_PASSWORD')
@click.option('--login-api', envvar='ACCOUNT_USER_API',
              default='local')
@click.option('--output', '-O', envvar='TOKEN_OUTPUT_PATH')
def token(username, password, login_api, output):
    """
    创建用户

    ..note::
        login-api = local 适用于内网环境和测试用例

    """
    password = password or getpass('please input your password:')
    # info = login(username, password)
    # click.echo(info['token'])

    import requests

    if login_api.lower() == 'local':
        data = login(username, password)
    else:
        ret = requests.post(login_api, data={
            'username': username,
            'password': password
        })
        ret.raise_for_status()
        data = ret.json()
        pass

    if output:
        with open(output, 'w') as fp:
            fp.write(data['token'])
            pass
    click.echo(data['token'])
    pass
