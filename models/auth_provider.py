import enum
from sqlalchemy import Enum


class AuthProviderEnum(enum.Enum):
    'google'
    'github'


AuthProvider = Enum(AuthProviderEnum, name='auth_provider')
