import threading

from .exceptions import RequestContextProxyError, RequestContextError


class RequestContext(object):
    def __init__(self):
        self.__request_context = threading.local()

    def get_attr(self, key, default=None):
        return getattr(self.__request_context, key, default)

    def set_attr(self, key, value):
        try:
            getattr(self.__request_context, key)
        except AttributeError:
            raise RequestContextError.ObjExisted('{} already exist, can\'t replace'.format(key))
        return setattr(self.__request_context, key, value)

    def clear(self):
        return self.__request_context.__dict__.clear()

    def init_by_request(self, request):
        self.set_attr('request', request)
        self.set_attr('g', GObject())


class GObject(object):

    def get(self, name, default=None):
        return self.__dict__.get(name, default)

    def pop(self, name, default=None):
        return self.__dict__.pop(name, default)

    def setdefault(self, name, default=None):
        return self.__dict__.setdefault(name, default)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)


class RequestContextProxy(object):

    def __init__(self, wrapped_func, read_only=False):
        if not callable(wrapped_func):
            raise RequestContextProxyError.WrongWrappedFunc('wrapped_func must be callable')
        object.__setattr__(self, '_RequestContextProxy__wrapped_func', wrapped_func)
        object.__setattr__(self, 'read_only', read_only)

    def _get_obj(self):
        obj = self.__wrapped_func()
        if obj is None:
            raise RequestContextProxyError.ObjNotFound('wrapped_func return nothing')
        return obj

    @property
    def __dict__(self):
        try:
            return self._get_obj().__dict__
        except RequestContextProxyError.ObjNotFound:
            raise AttributeError('__dict__')

    def __repr__(self):
        return repr(self._get_obj())

    def __str__(self):
        return str(self._get_obj())

    def __dir__(self):
        return dir(self._get_obj())

    def __getattr__(self, name):
        return getattr(self._get_obj(), name)

    def __setattr__(self, key, value):
        if self.read_only:
            raise RequestContextProxyError.ObjReadOnly('you can\'t change a readonly obj')
        return setattr(self._get_obj(), key, value)

    def __delattr__(self, item):
        return delattr(self._get_obj(), item)
