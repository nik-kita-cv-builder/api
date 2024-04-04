from sqlmodel import Relationship
from models.avatar import Avatar
from models.education import Education
from models.experience import Experience
from models.language import Language
from models.skill import Skill
from .contacts_kvd import ContactsKvd


from sqlmodel import SQLModel, Field


class BaseProfile(SQLModel):
    summary: str | None
    name: str | None = Field(default='default')
    details: str | None


class FullProfile(BaseProfile):
    user_id: int = Field(foreign_key='users.id', nullable=False)
    avatar_id: int | None = Field(foreign_key='avatars.id')
    id: int | None = Field(default=None, primary_key=True)


class Profile(FullProfile, table=True):
    __tablename__ = "profiles"
    contacts: list[ContactsKvd] = Relationship()
    skills: list[Skill] = Relationship()
    education: list[Education] = Relationship()
    experience: list[Experience] = Relationship()
    avatar: Avatar = Relationship()
    languages: list[Language] = Relationship()
