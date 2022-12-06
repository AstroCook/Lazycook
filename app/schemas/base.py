from typing import List, Optional, Union
from uuid import UUID

from pydantic import BaseModel


class BasicModel(BaseModel):
    id: UUID
    disabled: bool = False
