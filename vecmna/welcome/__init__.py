"""
=============
Welcome 模块
=============

"""


def run_app(app):
    from .apis import api
    app.register_blueprint(api)
