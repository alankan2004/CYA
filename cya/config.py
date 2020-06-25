import os

SECRET_KEY = os.environ.get('SECRET_KEY')
PROPAGATE_EXCEPTIONS = True

SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = [
    "access",
    "refresh",
]
JWT_ACCESS_TOKEN_EXPIRES = 1800