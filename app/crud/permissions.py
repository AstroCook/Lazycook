from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session

from app import models
from app.crud import authentication as crud_auth
from app.exceptions import not_found_exception, privlige_exception
from app.schemas import admins as schemas_admins


def get_users_by_access_level(db: Session, access_level: int):
    return db.query(models.User).filter(models.User.permissions == access_level).all()


def get_all_admins(db: Session):
    return db.query(models.Admin).all()


def get_admin_by_admin_id(db: Session, uuid: UUID):
    admin = db.query(models.Admin).filter(models.Admin.id == uuid).first()
    if admin:
        return admin
    raise not_found_exception


def get_user_access_level_from_id(db: Session, uuid: UUID):
    admin = db.query(models.Admin).filter(models.Admin.user_id == uuid).first()
    if admin:
        return admin.access_level
    raise not_found_exception


def add_admin(db: Session, admin: schemas_admins.CreateAdmin):
    user = db.query(models.User).filter(models.User.id == admin.user_id).first()
    if user:
        db_admin = models.Admin(**admin.dict())
        db.add(db_admin)
        db.commit()
        db.refresh(db_admin)
        return db_admin
    raise not_found_exception


def remove_admin(db: Session, user: models.User, admin_id: UUID):
    user_access_level = get_user_access_level_from_id(db=db, uuid=user.id)
    if (
        user_access_level <= 2
        and user_access_level > get_admin_by_admin_id(db=db, uuid=admin_id)
    ) or user_access_level == 1:
        admin = get_admin_by_id(db=db, admin_id=admin_id)
        if admin:
            db.delete(admin)
            db.commit()
        else:
            raise not_found_exception
    else:
        raise privlige_exception
