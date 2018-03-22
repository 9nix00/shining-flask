"""
=============
配置文件
=============
"""

import os

DEBUG = True if os.environ.get('FLASK_DEBUG', 'no') == 'yes' else False
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    'mysql+pymysql://root:root@127.0.0.1:3306/stormxx?charset=utf8mb4')

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
    'DB': os.environ.get('FLASK_MONGODB_DB', 'stormxx'),
    'HOST': os.environ.get('FLASK_MONGODB_HOST', '127.0.0.1'),
}

SECURITY_LOGIN_WITHIN = os.environ.get('SECURITY_LOGIN_WITHIN', '30 days')
SECURITY_PASSWORD_HASH = os.environ.get('SECURITY_PASSWORD_HASH',
                                        'sha256_crypt')
SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', 'I Use Hive')
SECURITY_LOGIN_SALT = os.environ.get('SECURITY_LOGIN_SALT', 'I Use Hive Login')
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'I Use Hive SECRET')

# OCR 配置
OCR_TESSERACT_BIN = '/usr/local/bin/tesseract'
OCR_TESSERACT_RESOURCE = '/usr/local/share/tessdata'
OCR_TESSERACT_DEFAULT_LANG = 'chi_sim'
OCR_TESSERACT_DEFAULT_PSM = 6

WEPUB_SAFE_DOMAIN = os.environ.get('WEPUB_SAFE_DOMAIN')

WEPAY_APP_ID = ACCOUNT_WEAPP_APP_ID
WEPAY_APP_SECRET = os.environ.get('WEPAY_APP_SECRET')
WEPAY_BUSINESS_ID = os.environ.get('WEPAY_BUSINESS_ID')
WEPAY_CALLBACK = 'https://%s/shopping/simple/confirm/wepay/%%(order_id)s' % \
                 os.environ.get('WEPAY_CALLBACK_DOMAIN')
WEPAY_SANDBOX_ACTIVE = False if os.environ.get(
    'WEPAY_SANDBOX_ACTIVE', 'no') != 'yes' else True

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

MARKET_WECHAT_SAFE_REGXP = os.environ.get('MARKET_WECHAT_SAFE_REGXP',
                                          str('^https://nextoa\.com|'
                                              '^https://stormxx\.com|'
                                              '^https://2shaoye\.com'))

WECHAT_TOKEN_KEY = os.environ.get('WECHAT_TOKEN_KEY', 'fantasy')
