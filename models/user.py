from tokenize import String
from sqlalchemy import Column
from models.base import BaseModel, gen_user_to_many
from auth_provider import AuthProvider


class BaseUser(BaseModel):
    __tablename__ = 'users'

    auth_provider = Column(AuthProvider, nullable=False)
    auth_id = Column(String, nullable=False)


class User(BaseUser):
    pass


class OrmUser(User):
    profiles = gen_user_to_many('Profile')
