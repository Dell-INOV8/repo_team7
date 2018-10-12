from backend.extensions import db
from backend.utils import get_class_by_tablename


user_model = get_class_by_tablename("user")


type_association = db.Table(
    'type_association', db.metadata,
    db.Column("id", db.Integer, primary_key=True),
    db.Column('left_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('post_type.id'))
)


user_association = db.Table(
    'user_association', db.metadata,
    db.Column("id", db.Integer, primary_key=True),
    db.Column('left_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('post.id'))
)


class PostType(db.Model):
    __tablename__ = "post_type"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, unique=True)
    active = db.Column(db.Boolean, default=True)

    def __str__(self):
        return str(self.type)


class Post(db.Model):
    __tablename__ = "post"
    __repr_attr__ = ("id", "type")

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)

    # Type information
    type = db.relationship(PostType, secondary=type_association)

    # Connect the post to its user
    user = db.relationship(user_model, secondary=user_association)
