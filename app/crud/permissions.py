from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session

from app import models
from app.crud import authentication as crud_auth
from app.schemas import admins as schemas_admins


def get_users_by_access_level(db: Session, access_level: int):
    return db.query(models.User).filter(models.User.permissions == access_level).all()

def get_all_admins(db: Session):
    return db.query(models.Admin).all()

def get_admin_by_admin_id(db: Session, uuid: UUID):
    return db.query(models.Admin).filter(models.Admin.id == uuid).first()

def get_user_access_level_from_id(db: Session, uuid: UUID):
    admin = db.query(models.Admin).filter(models.Admin.user_id == uuid).first()
    return admin.access_level

def add_admin(db: Session, admin: schemas_admins.CreateAdmin):
    # user_id = admin.user_id
    # db.user = models.User(**{"":""})
    db_admin = models.Admin(**admin.dict())
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def remove_admin(db: Session, user: models.User, admin_id: UUID):
    # TODO: Implement "admins" table
    if True:
        db_admin = get_allergy_by_id(db=db, allergy_id=allergy_id)
        db.delete(db_allergy)
        db.commit()
        return "Admin removed"
    raise crud_auth.privlige_exception
