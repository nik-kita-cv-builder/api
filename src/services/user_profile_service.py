from pydantic import BaseModel
from models.avatar import Avatar
from models.contacts_kvd import ContactsKvd, ContactsKvd
from models.education import Education
from models.experience import Experience
from models.language import Language
from models.profile import Profile
from sqlmodel import Session, select
from models.skill import Skill
from models.user import User


def gen_default_profile(user: User, session: Session):
    default_profile = Profile(user_id=user.id)
    session.add(default_profile)
    session.commit()
    session.refresh(default_profile)

    return default_profile


def get_user_profile(*, user_id: int, profile_name: str, session: Session):
    sql_query = select(Profile).where(
        Profile.user_id == user_id,
        Profile.name == profile_name,
    )
    profile = session.exec(sql_query).first()

    return profile


class UpsertProfile(BaseModel):
    contacts: list[ContactsKvd] | None = None
    skills: list[Skill] | None = None
    education: list[Education] | None = None
    experience: list[Experience] | None = None
    languages: list[Language] | None = None
    avatar: Avatar | None = None


def upsert_profile(
    *,
    user_id: int,
    profile_name: str,
    data: UpsertProfile,
    session: Session,
):
    profile = get_user_profile(
        user_id=user_id, profile_name=profile_name, session=session)

    if not profile:
        profile = Profile(
            user_id=user_id,
            name=profile_name,
        )

    if data.contacts:
        for c in data.contacts:
            c.user_id = user_id
        profile.contacts.extend(data.contacts)

    session.add(profile)
    session.commit()
    session.refresh(profile)

    return profile