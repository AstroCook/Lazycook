from typing import List, Optional, Union
from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import BasicModel

from app.schemas.allergies import ShowAllergy

class BaseIngridientAllergy(BasicModel):
    ingridient_id = UUID
    allergy_id = UUID

class ShowIngridientAllergy(BaseModel):
    ingridient_id = UUID
    allergy_id = UUID

    allergy = ShowAllergy

class CreateIngridientAllergy(BaseModel):
    ingridient_id = UUID
    allergy_id = UUID

class BaseIngridient(BasicModel):
    name = Column(str)
    allergens = Union[List[ShowIngridientAllergy], Optional[ShowIngridientAllergy]] = []

class ShowIngridient(BaseModel):
    name = Column(str)

class CreateIngridient(BaseModel):
    name = Column(str)