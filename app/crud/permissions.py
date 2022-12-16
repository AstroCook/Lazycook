from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session

from app import models
from app.crud import authentication as crud_auth
from app.schemas import admins as schemas_admins
from app.exceptions import privlige_exception, not_found_exception


def get_users_by_access_level(db: Session, access_level: int):
    return db.query(models.User).filter(models.User.permissions == access_level).all()


def get_all_admins(db: Session):
    return db.query(models.Admin).all()


def get_admin_by_admin_id(db: Session, uuid: UUID):
    return db.query(models.Admin).filter(models.Admin.id == uuid).first()


def get_user_access_level_from_id(db: Session, uuid: UUID):
    try:
        admin = db.query(models.Admin).filter(models.Admin.user_id == uuid).first()
        return admin.access_level
    except AttributeError:
        raise privlige_exception

def add_admin(db: Session, admin: schemas_admins.CreateAdmin):
    db_admin = models.Admin(**admin.dict())
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def remove_admin(db: Session, user: models.User, admin_id: UUID):
    try:
        db_admin = get_admin_by_id(db=db, admin_id=admin_id)
    except NameError:
        raise not_found_exception
    else:
        if get_acl(db=db, uuid=user.id) < 3:
            db.delete(db_admin)
            db.commit()
            return "Admin removed"
        raise privlige_exception
