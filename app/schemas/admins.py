from enum import IntEnum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import BasicModel


class permissions(IntEnum):
    head_admin = 1
    admin = 2


class BaseAdmin(BasicModel):
    access_level: permissions
    user_id: UUID


class AdminUnderUser(BaseModel):
    class Config:
        orm_mode = True

    access_level: permissions


class CreateAdmin(BaseModel):
    access_level: permissions
    user_id: UUID
