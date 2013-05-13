# coding: utf-8

import inspect


class StaticMethodsMetaclass(type):
    """Makes all non-magic methods static.
    """

    def __new__(mcs, name, parents, attrs):
        attrs = dict(((name, staticmethod(value),)
                      for name, value
                      in attrs.items()
                      if not name.startswith('__') and inspect.ismethod(value)))

        return type.__new__(mcs, name, parents, attrs)