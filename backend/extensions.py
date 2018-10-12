from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from .models import BaseModel


debug = DebugToolbarExtension()
boot = Bootstrap()
nav = Nav()
db = SQLAlchemy(model_class=BaseModel)
admin = Admin(template_mode='bootstrap3')
