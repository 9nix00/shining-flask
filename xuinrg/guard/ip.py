"""
=============
IP相关的限制
=============

此处大部分代码，参考自 `CTFd` <https://github.com/CTFd/CTFd>_

"""

import functools
import re

from flask import current_app as app, request, jsonify


def get_ip(req=None):
    """ Returns the IP address of the currently in scope request.
    The approach is to define a list of trusted proxies
     (in this case the local network),
     and only trust the most recently defined untrusted IP address.
     Taken from http://stackoverflow.com/a/22936947/4285524
      but the generator there makes no sense.
     The trusted_proxies regexes is taken from Ruby on Rails.

     This has issues if the clients are also on the local network
      so you can remove proxies from config.py.

     CTFd does not use IP address
     for anything besides cursory tracking of teams and
      it is ill-advised to do much
     more than that if you do not know what you're doing.
    """
    if req is None:
        req = request
    trusted_proxies = app.config.get('TRUSTED_PROXIES', [])
    combined = "(" + ")|(".join(trusted_proxies) + ")"
    route = req.access_route + [req.remote_addr]
    for addr in reversed(route):
        # IP is not trusted but we trust the proxies
        if not re.match(combined, addr):
            remote_addr = addr
            break
    else:
        remote_addr = req.remote_addr
    return remote_addr


def ratelimit(method="POST", limit=50, interval=300, key_prefix="rl"):
    """
    :param method:
    :param limit:
    :param interval:
    :param key_prefix:
    :return:
    """

    def ratelimit_decorator(f):
        cache = app.cache

        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            ip_address = get_ip()
            key = "{}:{}:{}".format(key_prefix, ip_address, request.endpoint)
            current = cache.get(key)

            if request.method == method:
                if current and int(
                        current) > limit - 1:
                    # -1 in order to align expected limit with the real value
                    resp = jsonify({
                        'code': 429,
                        "message": "Too many requests. "
                                   "Limit is %s requests in %s seconds" % (
                                       limit, interval)
                    })
                    resp.status_code = 429
                    return resp
                else:
                    if current is None:
                        cache.set(key, 1, timeout=interval)
                    else:
                        cache.set(key, int(current) + 1, timeout=interval)
            return f(*args, **kwargs)

        return decorated_function

    return ratelimit_decorator
