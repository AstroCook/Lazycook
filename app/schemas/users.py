from typing import List, Optional, Union

from pydantic import BaseModel

from app.schemas.admins import AdminUnderUser, BaseAdmin
from app.schemas.allergies import UserAllergyShow
from app.schemas.base import BasicModel


class UserBase(BasicModel):
    username: str
    name: str
    surname: str
    avatar_url: str
    description: Optional[str]

    allergies: Union[List[UserAllergyShow], UserAllergyShow] = []
    access_level: Optional[BaseAdmin]


class UserInDB(UserBase):
    password: str


class CreateUser(BaseModel):
    username: str
    name: Optional[str]
    surname: Optional[str]
    password: str
    avatar_url: str
    description: Optional[str]
