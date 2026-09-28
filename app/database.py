from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base

engine = create_engine("sqlite:///./tasks.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
