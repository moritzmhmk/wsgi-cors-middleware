WSGI-CORS-Middleware
====================

Cross Origin Resource Sharing (CORS) Middleware for WSGI Applications.

Usage
-----

Use the ``CorsMiddleware`` from ``wsgi_cors_middleware``.

.. code:: python

    from wsgi_cors_middleware import CorsMiddleware
    application = CorsMiddleware(
        application,
        origin='*',
        methods=['POST', 'PUT'],
        headers=['Content-Type', 'Authorization']
    )

Options
~~~~~~~

- ``origin``: URI that may access this application
- ``credentials``: indicates that the request can be made using credentials
- ``headers``: list of headers that may be used when accessing this application
- ``methods``: list of methods allowed to access this application
- ``expose_headers``: list of headers to be exposed to the browser
- ``max_age``: number of seconds a preflight request may be cached
