# Define models
from flask import url_for
from flask_admin import helpers as admin_helpers
from flask_security import SQLAlchemyUserDatastore, Security
from flask_security.utils import hash_password
from backend import admin, app
from .models import db, Role, User
from .views import SecurityAdmin


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()

    user_datastore.create_role(name="user")
    user_datastore.create_role(name="superuser")

    user_datastore.create_user(
        first_name='Admin',
        email='admin',
        password=hash_password('password'),
        roles=["user", "superuser"]
    )

    db.session.commit()


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )
