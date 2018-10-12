from flask import Flask, render_template
from flask_security import login_required
from .extensions import admin, boot, db, debug, ma, nav
from .models import BaseModel

# Create app context
app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../static"
)

# Create core context
import backend.core
import backend.navigation
db.init_app(app)
BaseModel.set_session(db.session)


@app.route("/")
@login_required
def index():
    return render_template("layout.html")


# Import modules
import backend.postings


# Register extensions
admin.init_app(app)
boot.init_app(app)
ma.init_app(app)
nav.init_app(app)

if app.config["DEBUG"]:
    debug.init_app(app)
