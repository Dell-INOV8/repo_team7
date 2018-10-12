import os


SITE_NAME = os.getenv("SITE_NAME", "TEAM 7")
DEBUG = os.getenv("DEBUG", True)
SECRET_KEY = os.getenv("SECRET_KEY", "{}".format(os.urandom(10)))
