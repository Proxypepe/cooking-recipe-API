from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.db.base_class import Base

SQLALCHEMY_DATABASE_URI = "sqlite:///D:/Projects/pythonProjects/cooking_recipe_API/example.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
