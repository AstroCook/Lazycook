from typing import List, Optional
from enum import IntEnum
from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import BasicModel

class permissions(IntEnum):
    head_admin = 1

class BaseAdmin(BasicModel):
    access_level: permissions
    user_id: UUID

class CreateAdmin(BaseModel):
    access_level: permissions
    user_id: UUID