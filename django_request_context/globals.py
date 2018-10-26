from functools import partial

from .request_context import RequestContextProxy, RequestContext


request_context = RequestContext()
request = RequestContextProxy(partial(request_context.get_attr, 'request'), True)
g = RequestContextProxy(partial(request_context.get_attr, 'g'))
