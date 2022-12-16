from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.crud import allergies as crud_allergies
from app.crud import authentication as crud_auth
from app.database import get_db
from app.schemas import allergies as schemas_allergies

router = APIRouter()


@router.get("")
def read_allergies(
    skip: int = 0,
    limit: int = 25,
    db: Session = Depends(get_db),
):
    return crud_allergies.get_all_allergies(db=db, skip=skip, limit=limit)


@router.get("/{allergy_id}")
def read_allergy_by_id(allergy_id: UUID, db: Session = Depends(get_db)):
    return crud_allergies.get_allergy_by_id(db=db, allergy_id=allergy_id)


@router.post("")
def create_allergy(
    allergy: schemas_allergies.CreateAllergy,
    db: Session = Depends(get_db),
    user: models.User = Depends(crud_auth.get_current_active_user),
):
    return crud_allergies.create_allergy(db=db, allergy=allergy)


@router.delete("")
def remove_allergy(
    allergy_id: UUID,
    db: Session = Depends(get_db),
    user: models.User = Depends(crud_auth.get_current_active_user),
):
    return crud_allergies.remove_allergy(db=db, allergy_id=allergy_id, user=user)
