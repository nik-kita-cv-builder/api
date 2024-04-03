from pydantic import BaseModel
from fastapi import HTTPException
from models.auth_provider import AuthProviderEnum


class SignIn(BaseModel):
    auth_provider: AuthProviderEnum
    auth_id: str


class SignInSuccess(BaseModel):
    access_token: str
    refresh_token: str
    type: str = 'bearer'


class SingInFail(HTTPException):
    def __init__(self, detail: str = 'Sign in failed'):
        super().__init__(status_code=401, detail=detail)


class JwtPayload(BaseModel):
    id: int
