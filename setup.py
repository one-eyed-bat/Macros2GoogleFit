from setuptools import setup, find_packages

setup(
        name='macros-2-googlefit',
        version='1.0',
        packages=find_packages(),
        install_requires=[
            'google-api-python-client',
            'google-auth',
            'google-auth-oauthlib',
            'google-auth-httplib2',
            'health-connect-client',
            'kivy',
            'android',
            'jnius',
            'packaging',
            'cython',
            'openssl'
            ],
        )

