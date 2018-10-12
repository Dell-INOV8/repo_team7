from backend import app


with app.app_context():
    app.config.from_pyfile("core/config.py")
