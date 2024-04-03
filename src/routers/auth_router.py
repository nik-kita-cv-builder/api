from fastapi import APIRouter

from schemas import auth


auth_router = APIRouter(tags=['Auth'])


@auth_router.post('/sign-in')
def sign_in(body: auth.SignIn):
    pass
