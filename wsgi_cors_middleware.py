"""Cross Origin Resource Sharing Middleware for WSGI Applications."""


class CorsMiddleware(object):
    """WSGI Middleware to enable Cross Origin Resource Sharing."""

    def __init__(
        self,
        application,
        origin='*',
        credentials=False,
        headers=[],
        methods=[],
        expose_headers=[],
        max_age=600
    ):
        """Create Middleware with headers for given options."""
        self.application = application

        # headers that are part of both preflight and regular cors requests
        self.cors_headers = [('Access-Control-Allow-Origin', origin)]
        if credentials:  # do not include header if false
            self.cors_headers.append(('Access-Control-Allow-Credentials',
                                      'true'))

        # headers that are only part of preflight responses
        self.cors_preflight_headers = [
            ('Access-Control-Allow-Headers', ', '.join(headers)),
            ('Access-Control-Allow-Methods', ', '.join(methods)),
            ('Access-Control-Max-Age', str(max_age))
        ]

        # headers that are not part of preflight responses
        self.cors_non_preflight_headers = [
            ('Access-Control-Expose-Headers', ', '.join(expose_headers))
        ]

    def __call__(self, environ, start_response):
        """Handle preflight and inject CORS headers to responses."""
        # respond to CORS preflight request
        if (
            environ.get('REQUEST_METHOD', '').lower() == 'options' and
            environ.get('HTTP_ACCESS_CONTROL_REQUEST_METHOD') is not None
        ):
            start_response(
                '200 OK',
                self.cors_headers + self.cors_preflight_headers
            )
            return []

        # inject cors headers in all responses
        def wrapped_start_response(status, headers):
            start_response(
                status,
                headers + self.cors_headers + self.cors_non_preflight_headers
            )

        return self.application(environ, wrapped_start_response)
