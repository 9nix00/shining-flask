"""
=============
App Config
=============
"""

import os

DEBUG = True if os.environ.get('FLASK_DEBUG', 'no') == 'yes' else False
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    'mysql+pymysql://root:root@127.0.0.1:3306/lego?charset=utf8mb4')

SQLALCHEMY_TRACK_MODIFICATIONS = True if os.environ.get(
    'SQLALCHEMY_TRACK_MODIFICATIONS', 'yes') == 'yes' else False

CACHE_TYPE = os.environ.get('FLASK_CACHE_TYPE', 'redis')
CACHE_REDIS_URL = os.environ.get('FLASK_REDIS_URL',
                                 'redis://127.0.0.1:6379/0')

JSON_AS_ASCII = True if os.environ.get('FLASK_JSON_AS_ASCII',
                                       'yes') == 'yes' else False

ACCOUNT_USERNAME_DISABLE_REGISTER = True if os.environ.get(
    'ACCOUNT_USERNAME_DISABLE_REGISTER',
    'yes') == 'yes' else False

ACCOUNT_WEAPP_DISABLE_REGISTER = True if os.environ.get(
    'ACCOUNT_USERNAME_DISABLE_REGISTER',
    'yes') == 'yes' else False

ACCOUNT_WEAPP_APP_ID = os.environ.get('ACCOUNT_WEAPP_APP_ID')
ACCOUNT_WEAPP_APP_SECRET = os.environ.get('ACCOUNT_WEAPP_APP_SECRET')

ACCOUNT_WEPUB_APP_ID = os.environ.get('ACCOUNT_WEPUB_APP_ID')
ACCOUNT_WEPUB_APP_SECRET = os.environ.get('ACCOUNT_WEPUB_APP_SECRET')

MONGODB_SETTINGS = {
    'DB': os.environ.get('FLASK_MONGODB_DB', 'lego'),
    'HOST': os.environ.get('FLASK_MONGODB_HOST', '127.0.0.1'),
}

SECURITY_LOGIN_WITHIN = os.environ.get('SECURITY_LOGIN_WITHIN', '30 days')
SECURITY_PASSWORD_HASH = os.environ.get('SECURITY_PASSWORD_HASH',
                                        'sha256_crypt')
SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', 'I Use Hive')
SECURITY_LOGIN_SALT = os.environ.get('SECURITY_LOGIN_SALT', 'I Use Hive Login')
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'I Use Hive SECRET')

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
