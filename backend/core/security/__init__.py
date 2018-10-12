# Define models
from flask_security import SQLAlchemyUserDatastore, Security
from backend import app
from .models import db, Role, User


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='admin@email.net', password='password')
    db.session.commit()
    print("created user")
