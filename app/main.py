from typing import List

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app import crud, models, schemas
from app.database import engine
from app.endpoints.allergies import router as allergies_router
from app.endpoints.authentication import router as authentication_router
from app.endpoints.users import router as users_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

api_router = APIRouter()
api_router.include_router(authentication_router, prefix="", tags=["auth"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(allergies_router, prefix="/allergies", tags=["allergies"])

origins = ["*"]

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
