class DefaultConfig(object):

    DEBUG = True
    TESTING = False

    DB_NAME = "database.db"

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
    SECRET_KEY = "flaskstarter"