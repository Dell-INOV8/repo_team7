from backend import admin, app

with app.app_context():
    import backend.postings.models
    import backend.postings.views
    models.db.create_all()
    admin.add_view(
        views.PostingView(
            models.Post, models.Post.session, name='Manage Posts', category='Post Admin'
        )
    )
    admin.add_view(
        views.PostingView(
            models.PostType, models.PostType.session, name='Manage Post Types', category='Post Admin'
        )
    )
