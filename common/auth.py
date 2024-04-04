from typing import Annotated
from fastapi import Depends
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from common.config import (
    SWAGGER_HELPER_URL,
    ACCESS_SECRET_KEY,
    ALGORITHM,
)
from models.user import User, get_user_by_id
from utils.jwt import get_payload_from_token
from common.db import Db


_oauth2_schema = HTTPBearer(
    description=f"""
#### How to get access token
1. [Sign in with Google]({SWAGGER_HELPER_URL})
2. Token from step 1 should be used in `/sign-in` endpoint
3. Access token from `/sign-in` insert into input below
""",
)


def _get_me(
    auth_credentials: Annotated[HTTPAuthorizationCredentials, Depends(_oauth2_schema)],
    session: Db,
):
    payload = get_payload_from_token(
        token=auth_credentials.credentials,
        secret=ACCESS_SECRET_KEY,
        algorithms=[ALGORITHM],
    )
    me = get_user_by_id(payload["id"], session)
    print(me)
    return me, session


Me_and_Session = Annotated[tuple[User | None, Db], Depends(_get_me)]