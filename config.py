import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = 'mongodb://192.168.1.103:32017/kafkaconnect'


class TestingConfig(Config):
    TESTING = True
    MONGO_URI = 'mongodb://192.168.1.103:32017/kafkaconnect'


class ProductionConfig(Config):
    MONGO_URI = 'mongodb://192.168.1.103:32017/kafkaconnect'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
