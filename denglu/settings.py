class BaseConfig(object):
    DEBUG = True
    SESSION_COOKIE_NAME = "session_sss"

class TestConfig(BaseConfig):
    DB = "127.0.0.1"

class DevConfig(BaseConfig):
    DB = "52.5.7.5"

class ProConfig(BaseConfig):
    DB = "55.4.22.4"