import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PGUSER = os.environ.get("PGUSER", default="Maks")
PGPASSWORD = os.environ.get("PGPASSWORD", default="Maks")
PGHOST = os.environ.get("PGHOST", default="db")
PGPORT = ":" + os.environ.get("PGPORT", default="")
PGDATABASE = os.environ.get("PGDATABASE", default="lazycook")

SQLALCHEMY_DATABASE_URL = f"postgresql://{PGUSER}:{PGPASSWORD }@{PGHOST}{PGPORT}/{PGDATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
