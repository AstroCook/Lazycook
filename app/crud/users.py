from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session

from app import models
from app.crud import authentication as crud_auth
from app.schemas import users as schemas_users
from app.crud.permissions import get_user_access_level_from_id as get_acl


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_schema_by_username(db: Session, username: str):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    return schemas_users.UserInDB(**db_user.__dict__)


def get_users(db: Session, user: models.User, skip: int = 0, limit: int = 25):
    if get_acl(db=db, uuid=user.id) < 3:
        return db.query(models.User).all()
    else:
        raise crud_auth.privlige_exception


def get_user_by_id(db: Session, user_id: UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas_users.CreateUser):
    hashed_password = crud_auth.get_password_hash(user.password)
    db_user = models.User(
        **user.dict(exclude={"password", "date_of_creation", "date_of_last_edit"}),
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def remove_user(db: Session, user: models.User, user_id: UUID):
    try:
        db_user = get_user_by_id(db=db, user_id=user_id)
    except NameError:
        raise not_found_exception
    else:
        if get_acl(db=db, uuid=user.id) < 3:
            db_user = get_user_by_id(db=db, user_id=user_id)
            db.delete(db_user)
            db.commit()
        else:
            raise crud_auth.privlige_exception
