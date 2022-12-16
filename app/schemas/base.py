from typing import List, Optional, Union
from uuid import UUID

from pydantic import BaseModel


class BasicModel(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    disabled: bool = False
