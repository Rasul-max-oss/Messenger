from flask_sqlalchemy.session import Session
from sqlalchemy import create_engine, Column, Integer, String, PrimaryKeyConstraint, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.testing.plugin.plugin_base import engines

Base = declarative_base()
engine = create_engine("sqlite:///test.db")
SessionLocal = sessionmaker(bind=engine)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True)
    title =  Column(String)
    description = Column(String)
    is_completed = Column(Boolean,default=False)



