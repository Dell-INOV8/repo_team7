from backend import app


with app.app_context():
    app.config.from_pyfile("core/config.py")
    app.config.from_pyfile("core/security/config.py")
    import backend.core.security
