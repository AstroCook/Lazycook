from typing import List, Optional, Union

from pydantic import BaseModel

from app.schemas.allergies import UserAllergyShow
from app.schemas.admins import BaseAdmin
from app.schemas.base import BasicModel


class UserBase(BasicModel):
    username: str
    name: str
    surname: str
    avatar_url: str
    description: Optional[str]

    allergies: Optional[List[UserAllergyShow]]
    permissions: Optional[BaseAdmin]

class UserInDB(UserBase):
    password: str


class CreateUser(BaseModel):
    username: str
    name: Optional[str]
    surname: Optional[str]
    password: str
    avatar_url: str
    description: Optional[str]
