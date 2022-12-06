from datetime import datetime
from uuid import UUID

from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.crud import authentication as crud_auth
from app.crud import allergies as crud_allergies
from app.schemas import allergies as schemas_allergies

router = APIRouter()


@router.get("")
def read_allergies(
    skip: int = 0,
    limit: int = 25,
    db: Session = Depends(get_db),
):
    return crud_allergies.get_all_allergies(db=db, skip=skip, limit=limit)


# @router.get("/{user_id}")
# def read_user_by_id(user_id: UUID, db: Session = Depends(get_db)):
#     return crud_users.get_user_by_id(db=db, user_id=user_id)


# @router.post("")
# def create_user(user: schemas_users.CreateUser, db: Session = Depends(get_db)):
#     return crud_users.create_user(db=db, user=user)


# @router.delete("")
# def remove_user(
#     user_id: UUID,
#     db: Session = Depends(get_db),
#     user: models.User = Depends(crud_auth.get_current_active_user),
# ):
#     return crud_users.remove_user(db=db, user_id=user_id, user=user)