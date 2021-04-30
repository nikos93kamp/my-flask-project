import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY_2')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    ENV = 'dev'

    if ENV == 'dev':
        DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        DEBUG = (os.environ.get('DEBUG_VALUE') != 'True')
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
