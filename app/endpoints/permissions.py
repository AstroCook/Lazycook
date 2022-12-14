from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.crud import permissions as crud_perm
from app.crud import authentication as crud_auth
from app.database import get_db
from app.schemas import admins as schema_perm

router = APIRouter()


@router.get("")
def read_admins(
    db: Session = Depends(get_db),
):
    return crud_perm.get_all_admins(db=db)


@router.get("/{admin_id}")
def read_admin_by_id(admin_id: UUID, db: Session = Depends(get_db)):
    return crud_perm.get_admin_by_admin_id(db=db, uuid=admin_id)


@router.post("")
def create_admin(perm: schema_perm.CreateAdmin, db: Session = Depends(get_db), user: models.User = Depends(crud_auth.get_current_active_user)):
    return crud_perm.add_admin(db=db, admin=perm)


@router.delete("")
def remove_admin(
    admin_id: UUID,
    db: Session = Depends(get_db),
    user: models.User = Depends(crud_auth.get_current_active_user),
):
    return crud_perm.remove_admin(db=db, admin_id=admin_id, user=user)
