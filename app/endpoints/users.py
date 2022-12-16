from datetime import datetime
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.crud import authentication as crud_auth
from app.crud import users as crud_users
from app.database import get_db
from app.schemas import users as schemas_users

router = APIRouter()


@router.get("")
def read_users(
    skip: int = 0,
    limit: int = 25,
    db: Session = Depends(get_db),
    user: models.User = Depends(crud_auth.get_current_active_user),
):
    return crud_users.get_users(db=db, skip=skip, limit=limit, user=user)


@router.get("/{user_id}", response_model=schemas_users.UserBase)
def read_user_by_id(user_id: UUID, db: Session = Depends(get_db)):
    return crud_users.get_user_by_id(db=db, user_id=user_id)


@router.post("")
def create_user(user: schemas_users.CreateUser, db: Session = Depends(get_db)):
    return crud_users.create_user(db=db, user=user)


@router.delete("")
def remove_user(
    user_id: UUID,
    db: Session = Depends(get_db),
    user: models.User = Depends(crud_auth.get_current_active_user),
):
    return crud_users.remove_user(db=db, user_id=user_id, user=user)
