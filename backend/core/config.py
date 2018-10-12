import os


SITE_NAME = os.getenv("SITE_NAME", "TEAM 7")
DEBUG = os.getenv("DEBUG", True)
SECRET_KEY = os.getenv("SECRET_KEY", "{}".format(os.urandom(10)))
SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", "sqlite://")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("TRACK_DB_MODIFICATIONS", False)
