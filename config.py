import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-change-this'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:viki123@host.docker.internal:9090/museum_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
