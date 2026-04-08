from flask_sqlalchemy.session import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.testing.plugin.plugin_base import engines

Base = declarative_base()
engine = create_engine("sqlite:///test2.db")
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    age = Column(Integer)







