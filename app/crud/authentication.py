from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app import models
from app.crud import users as crud_users
from app.database import get_db
from app.schemas import tokens as schemas_tokens

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "ea6e3a7f19faafa7d311a300e3c88c84c48fc73b82e35b868af30bbc06450a35"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

privlige_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="User is not admin",
    headers={"WWW-Authenticate": "Bearer"},
)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, username: str, password: str):
    user = crud_users.get_user_schema_by_username(db=db, username=username)
    if not user:
        return False
    print(password, user.password)
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas_tokens.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    local_user = crud_users.get_user_schema_by_username(
        db=db, username=token_data.username
    )
    if local_user is None:
        raise credentials_exception
    return local_user


async def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
