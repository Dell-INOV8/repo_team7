from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy


debug = DebugToolbarExtension()
boot = Bootstrap()
nav = Nav()
db = SQLAlchemy()
