from setuptools import setup

version = '0.0.2'
url = 'https://github.com/moritzmhmk/wsgi-cors-middleware'
download_url = '{}/archive/v{}.tar.gz'.format(url, version)

setup(
    name='wsgi-cors-middleware',
    py_modules=['wsgi_cors_middleware'],
    version=version,
    description='Cross Origin Resource Sharing (CORS) Middleware for WSGI Applications.',
    long_description=open('README.rst').read(),
    author='Moritz K.',
    author_email='moritzmhmk@googlemail.com',
    url=url,
    download_url=download_url,
    license='MIT',
    keywords=['wsgi', 'cors', 'middleware'],
    classifiers=[],
)
