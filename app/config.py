import os

class Config:
    SECRET_KEY = '8f9ee75239853cee393a15d286bb26f8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER', 'anlaptrinhweb97@gmail.com')
    MAIL_PASSWORD  = os.environ.get('EMAIL_PASS', 'nguyenminhan')