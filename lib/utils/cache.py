# coding: utf-8

import hashlib
import os

_cache_base_path = os.path.join(os.getcwd(), 'cache')

_initialized = False


def init():
    global _initialized

    if _initialized:
        return

    if not os.path.exists(_cache_base_path):
        os.makedirs(_cache_base_path)

    _initialized = True


def _get_file_path(name):
    return os.path.join(_cache_base_path, '%s.cached' % _hash(name))


def _hash(name):
    return hashlib.md5(name).hexdigest()


def is_stored(name):
    return os.path.exists(_get_file_path(name))


def put(name, value):
    path = _get_file_path(name)

    if is_stored(name):
        return False

    init()

    with open(path, 'wb') as f:
        f.write(value)

    return True


def get(name):
    if is_stored(name):
        return open(_get_file_path(name), 'rb').read()

    return None