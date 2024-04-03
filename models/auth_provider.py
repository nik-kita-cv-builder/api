import enum
from sqlalchemy import Enum


class AuthProviderEnum(str, enum.Enum):
    'google'
    'github'


AuthProvider = Enum(AuthProviderEnum, name='auth_provider')
