from pydantic import BaseModel

from models.avatar_model import Avatar
from models.contacts_model import ContactsKvd
from models.education_model import Education
from models.experience_model import Experience
from models.language_model import Language
from models.skill_model import Skill


class ProfileReq(BaseModel):
    user_id: int
    name: str
    summary: str | None = None
    details: str | None = None
    contacts: list[ContactsKvd] | None = None
    skills: list[Skill] | None = None
    education: list[Education] | None = None
    experience: list[Experience] | None = None
    languages: list[Language] | None = None
    avatar: Avatar | None = None


class ProfileRes(BaseModel):
    id: int
    user_id: int
    name: str
    summary: str | None = None
    details: str | None = None
    contacts: list[ContactsKvd] = []
    skills: list[Skill] = []
    education: list[Education] = []
    experience: list[Experience] = []
    avatar: Avatar | None = None
    languages: list[Language] = []
