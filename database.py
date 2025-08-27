from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./aeternum.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} #requisito de SQLite para FastAPI pueda manejar varias peticiones.
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #sesión de base de datos se usa en cada enpoint de la API.

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
