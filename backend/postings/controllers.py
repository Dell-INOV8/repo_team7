from flask import jsonify
from flask_restful import Resource, reqparse
from flask_security import current_user
from .models import Post
from .serializers import post_schema
from backend.utils import get_class_by_tablename

user_model = get_class_by_tablename("user")


class PostApi(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("body")
        self.args = parser.parse_args()
        super().__init__()

    def get(self):
        user = user_model.find(int(current_user.id) if current_user and hasattr(current_user, "id") else 1)
        return jsonify(
            data=post_schema.dumps(user.posts).data
        )

    def post(self):
        post = Post.create(body=self.args['body'])
        user = user_model.find(int(current_user.id) if current_user and hasattr(current_user, "id") else 1)
        user.posts.append(post)
        Post.session.commit()
        return jsonify(201, "Created post.")
