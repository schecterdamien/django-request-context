

class RequestContextProxyError(object):

    class WrongWrappedFunc(Exception):
        pass

    class ObjNotFound(Exception):
        pass

    class ObjReadOnly(Exception):
        pass


class RequestContextError(object):

    class ObjExisted(Exception):
        pass
