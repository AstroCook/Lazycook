from typing import List, Optional
from enum import Enum, IntEnum

from pydantic import BaseModel

from app.schemas.base import BasicModel

class permissions(Enum):
    head_admin = 1

class BaseAdmin(BasicModel):
    access_level = IntEnum(permissions)
    allergies: Optional[List[UserAllergyShow]]

class CreateAdmin(BaseModel):
    access_le