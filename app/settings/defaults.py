import os


class Config(object):
    APP_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    STATIC_PATH = os.path.join(APP_ROOT, 'app', 'static')
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/make_happy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'bigbigsecret'


class DevelopmentConfig(Config):
    """
    Settings used for development
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    """
    Settings used by the test runner
    """
    TESTING = True
    TRAP_HTTP_EXCEPTIONS = True
    TRAP_BAD_REQUEST_ERRORS = True
    SQLALCHEMY_ECHO = True
