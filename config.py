from email.policy import default
import os
from decouple import config

class Config:
    """
    General configuration parent class
    """
    DB_USER = config('DB_USER', default="")
    DB_PASSWORD = config('DB_PASSWORD', default="")
    DB = 'pitches'

    UPLOADED_PHOTOS_DEST ='app/static/uploads'
    
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost/{DB}'

    SECRET_KEY = config('SECRET_KEY', default="")



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URL", default="").replace("postgres://", "postgresql://", 1)


class DevelopmentConfig(Config):
    DEBUG = True


config_options = {
    'development': DevelopmentConfig,
    'production': ProdConfig
}