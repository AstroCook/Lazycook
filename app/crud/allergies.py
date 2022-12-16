from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session

from app import models
from app.crud import authentication as crud_auth
from app.schemas import allergies as schemas_allergies


def get_allergy_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.Allergy.name == name).first()


def get_all_allergies(db: Session, skip: int = 0, limit: int = 25):
    return db.query(models.Allergy).offset(skip).limit(limit).all()


def get_allergy_by_id(db: Session, allergy_id: UUID):
    return db.query(models.Allergy).filter(models.Allergy.id == allergy_id).first()


def create_allergy(db: Session, allergy: schemas_allergies.CreateAllergy):
    if get_acl(db=db, uuid=user.id) < 3:
        db_allergy = models.Allergy(**allergy.dict())
        db.add(db_allergy)
        db.commit()
        db.refresh(db_allergy)
        return db_allergy
    raise crud_auth.privlige_exception

def remove_allergy(db: Session, user: models.User, allergy_id: UUID):
    try:
        db_allergy = get_allergy_by_id(db=db, allergy_id=allergy_id)
    except NameError:
        raise not_found_exception
    else:
        if get_acl(db=db, uuid=user.id) < 3:
            db_allergy = get_allergy_by_id(db=db, allergy_id=allergy_id)
            db.delete(db_allergy)
            db.commit()
            return "Allergy removed"
        raise crud_auth.privlige_exception
