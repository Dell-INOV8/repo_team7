from backend import admin, app, db


with app.app_context():
    app.config.from_pyfile("core/config.py")
    app.config.from_pyfile("core/security/config.py")
    import backend.core.security
    admin.add_view(
        security.SecurityAdmin(
            security.User, db.session, name='Manage Users', category='User Admin'
        )
    )
    admin.add_view(
        security.SecurityAdmin(
            security.Role, db.session, name='Manage Roles', category='User Admin'
        )
    )
    print("added admin pages")

