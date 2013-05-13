# coding: utf-8

from lib.utils.metaclasses import StaticMethodsMetaclass


class Controller(object):
    """Parent class for all app's controllers.
    """

    __metaclass__ = StaticMethodsMetaclass