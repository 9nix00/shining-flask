"""
=============
测试用例
=============
"""

from flask import url_for


def test_hello(client):
    response = client.get(url_for('welcome.hello'))   # 创建请求
    assert 200 == response.status_code                # 比对http status code
    assert 'hello' in response.json.keys()            # 检查key是否存在
    assert 'world' == response.json['hello']          # 检查值是否正确
    pass
