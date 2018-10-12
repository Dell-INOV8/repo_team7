from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_marshmallow import Marshmallow
from .models import BaseModel


debug = DebugToolbarExtension()
boot = Bootstrap()
nav = Nav()
db = SQLAlchemy(model_class=BaseModel)
admin = Admin(base_template='admin_layout.html', template_mode='bootstrap3')
ma = Marshmallow()
