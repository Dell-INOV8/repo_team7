from backend import admin, app
from flask import Blueprint
from flask_restful import Api

postings_bp = Blueprint("postings_bp", __name__)
postings_api = Api(postings_bp)

with app.app_context():
    import backend.postings.models
    import backend.postings.views
    import backend.postings.controllers
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
    postings_api.add_resource(controllers.PostApi, "/api/postings")

app.register_blueprint(postings_bp)
