from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import BasicModel


class BaseAllergy(BasicModel):
    name: str


class ShowAllergy(BaseModel):
    name: str


class CreateAllergy(BaseModel):
    name: str


class BaseUserAllergy(BasicModel):
    user_id: UUID
    allergy_id: UUID


class UserAllergyShow(BaseModel):
    id: UUID
    allergies: Optional[List[ShowAllergy]]


class CreateUserAllergy(BasicModel):
    user_id: UUID
    allergy_id: UUID
