from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session

from app import models
from app.crud import authentication as crud_auth
from app.exceptions import not_found_exception
from app.schemas import allergies as schemas_allergies


def get_all_allergies(db: Session, skip: int = 0, limit: int = 25):
    return db.query(models.Allergy).offset(skip).limit(limit).all()


def get_allergy_by_name(db: Session, name: str):
    allergy = db.query(models.User).filter(models.Allergy.name == name).first()
    if allergy:
        return allergy
    raise not_found_exception


def get_allergy_by_id(db: Session, allergy_id: UUID):
    allergy = db.query(models.Allergy).filter(models.Allergy.id == allergy_id).first()
    if allergy:
        return allergy
    raise not_found_exception


def create_allergy(db: Session, allergy: schemas_allergies.CreateAllergy):
    if get_acl(db=db, uuid=user.id) <= 2:
        db_allergy = models.Allergy(**allergy.dict())
        db.add(db_allergy)
        db.commit()
        db.refresh(db_allergy)
        return db_allergy
    raise crud_auth.privlige_exception


def remove_allergy(db: Session, user: models.User, allergy_id: UUID):
    if get_acl(db=db, uuid=user.id) <= 2:
        allergy = get_allergy_by_id(db=db, allergy_id=allergy_id)
        if allergy:
            db_allergy = get_allergy_by_id(db=db, allergy_id=allergy_id)
            db.delete(db_allergy)
            db.commit()
        else:
            raise not_found_exception
    else:
        raise crud_auth.privlige_exception
