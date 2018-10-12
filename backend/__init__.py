from flask import Flask, render_template
from .extensions import debug

# Create app context
app = Flask(
    __name__,
    template_folder="../frontend"
)

# Import modules
import backend.core


@app.route("/")
def default():
    return render_template("layout.html")


if app.config["DEBUG"]:
    debug.init_app(app)
