from models.base import BaseModel, ManyToUser


class BaseProfile(BaseModel):
    __annotations__ = 'profiles'
    pass


class Profile(BaseProfile, ManyToUser):
    pass
