import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('POSTGRES_HOST')}:{os.environ.get('POSTGRES_PORT')}/{os.environ.get('POSTGRES_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# import os
#
# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'kiiiProekt2025'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:viki123@localhost:55432/museum_db'
#
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#

# import os
#
# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# 'postgresql://postgres:viki123@host.docker.internal:9090/museum_db'