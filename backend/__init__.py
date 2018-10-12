from flask import Flask, render_template
from .extensions import boot, debug, nav

# Create app context
app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../static"
)


@app.route("/")
def index():
    return render_template("layout.html")


# Import modules
import backend.core
import backend.navigation

# Register extensions
boot.init_app(app)
nav.init_app(app)

if app.config["DEBUG"]:
    debug.init_app(app)
