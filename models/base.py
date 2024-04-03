from deps import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class BaseModel(Base):
    id = Column(Integer, primary_key=True)


class ManyToUser:
    user_id = Column(Integer, ForeignKey('users.id'))


class ManyToProfile:
    profile_id = Column(Integer, ForeignKey('profiles.id'))


def gen_user_to_many(child_model: str):
    return relationship(child_model, cascade='all, delete-orphan')


def gen_profile_to_many(child_model: str):
    return relationship(child_model)
