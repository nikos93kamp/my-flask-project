import os
import flask_heroku


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY_2')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    DEBUG = True
    ALLOWED_HOSTS = ['myflaskapp3.herokuapp.com']

    flask_heroku.settings(locals())
