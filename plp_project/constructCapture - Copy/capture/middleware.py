# Example of a middleware in capture/middleware.py
import logging

logger = logging.getLogger(__name__)

class URLLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request URL: {request.path}")
        response = self.get_response(request)
        return response
