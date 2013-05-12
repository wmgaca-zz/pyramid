

class ControllerMetaclass(type):

    def __new__(mcs, name, parents, attrs):
        attrs = dict(((name, staticmethod(value),) for name, value in attrs.items() if not name.startswith('__')))
        return type.__new__(mcs, name, parents, attrs)


class Controller(object):

    __metaclass__ = ControllerMetaclass
