from sqlmodel import Relationship
from sqlalchemy import orm

from models.avatar_model import Avatar
from models.contact_model import Contact
from models.education_model import Education
from models.experience_model import Experience
from models.language_model import Language
from models.skill_model import Skill

from .profile_model import Profile
from .auth_provider_enum import AuthProvider, AuthProviderEnum
from sqlmodel import Field, SQLModel

relation_ondelete_delete = Relationship(
    sa_relationship=orm.relationship(
        Profile,
        cascade='all, delete-orphan',
    ))


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    email: str | None = Field(str, unique=True)
    sub: str | None = Field(str, unique=True)
    auth: AuthProviderEnum = Field(AuthProvider)

    profiles: list[Profile] = relation_ondelete_delete
    avatars: list[Avatar] = relation_ondelete_delete

    contacts: list[Contact] = relation_ondelete_delete
    skills: list[Skill] = relation_ondelete_delete
    educations: list[Education] = relation_ondelete_delete
    experiences: list[Experience] = relation_ondelete_delete
    languages: list[Language] = relation_ondelete_delete
