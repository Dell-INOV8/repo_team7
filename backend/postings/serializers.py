from backend import ma
from .models import Post


class SerialPost(ma.ModelSchema):
    class Meta:
        fields = ("body",)
        model = Post


post_schema = SerialPost(many=True)
