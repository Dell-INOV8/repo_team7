from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin


Base = declarative_base(name='Model')


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True

    @classmethod
    def find(cls, model_id):
        return cls.query.filter(cls.id == model_id).first()
