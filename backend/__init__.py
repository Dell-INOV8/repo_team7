from flask import Flask, render_template
from flask_security import login_required
from .extensions import admin, boot, db, debug, nav

# Create app context
app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../static"
)


@app.route("/")
@login_required
def index():
    return render_template("layout.html")


# Import modules
import backend.core
import backend.navigation

# Register extensions
admin.init_app(app)
boot.init_app(app)
db.init_app(app)
nav.init_app(app)

if app.config["DEBUG"]:
    debug.init_app(app)
