from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_ENGINE_URI = "sqlite:///example.db"

engine = create_engine(SQLALCHEMY_ENGINE,
                       connect_args={"check_thread": False}
                       )

SessionLocal = sessionmaker(autocommit=False, autoflush=False)

