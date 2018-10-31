Flask开发日常 - 你的账户模块设计对了吗
===========================================

[![Build Status](https://secure.travis-ci.org/wangwenpei/shining-flask.png?branch=master)](https://travis-ci.org/wangwenpei/shining-flask)
[![Code Coverage Status](https://codecov.io/github/wangwenpei/shining-flask/coverage.svg?branch=master)](https://codecov.io/github/wangwenpei/shining-flask?branch=master)


推荐开发环境
------------------

- pycharm
- macOS
- python3.5+

注意事项
-----------

* 我们不对python3.5以下版本及windows提供支持


知识储备要求[自行学习]
---------------------

- 了解web开发中账户的登录验证的基本原理
- 了解数据库基本概念 



快速预览
----------

```
pip install -r requirements.txt
pip install -r requirements.test.txt

# 确保本地mysql正常开启，用户名密码root:root。
# 或者变更默认配置
python manage.py ff migrate 
PYTHONPATH=. pytest accounts/username
```

