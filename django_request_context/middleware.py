# -*- coding: utf-8 -*-
from .globals import request_context

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10
    MiddlewareMixin = object


class RequestContextMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request_context.init_by_request(request)

    def process_response(self, request, response):
        request_context.clear()
        return response

