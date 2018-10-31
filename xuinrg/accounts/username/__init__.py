"""
=============
Username 方式
=============

用户名方式
"""


def run_app(app):
    from .apis import api

    app.register_blueprint(api)
    pass



def run_cli(app):
    from .commands import user
    app.cli.add_command(user)
    pass
