from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class BaseDatabaseModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date_of_creation = Column(DateTime(timezone=True), server_default=func.now())
    date_of_last_edit = Column(DateTime(timezone=True), onupdate=func.now())
    disabled = Column(Boolean, default=False)


class User(BaseDatabaseModel):
    __tablename__ = "users"

    username = Column(String)
    name = Column(String)
    surname = Column(String)
    password = Column(String)
    description = Column(String)
    avatar_url = Column(String)

    allergies = relationship("UserAllergy", back_populates="user")
    access_level = relationship("Admin", back_populates="user", uselist=False)


class Admin(BaseDatabaseModel):
    __tablename__ = "admins"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    access_level = Column(Integer)

    user = relationship("User", back_populates="access_level")


class UserAllergy(BaseDatabaseModel):
    __tablename__ = "user_allergies"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    allergy_id = Column(UUID(as_uuid=True), ForeignKey("allergies.id"))

    user = relationship("User", back_populates="allergies")
    allergy = relationship("Allergy", back_populates="users")


class Allergy(BaseDatabaseModel):
    __tablename__ = "allergies"

    name = Column(String)

    users = relationship("UserAllergy", back_populates="allergy")
