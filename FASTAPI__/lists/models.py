from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:////test2.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    health = Column(Integer, default=100)
    food = Column(Integer, default=100)
    energy = Column(Integer, default=100)
    money = Column(Float, default=0)
    day = Column(Integer, default=1)
    exp = Column(Integer, default=1)
    happiness = Column(Integer, default=100)

    # будем хранить как JSON строку
    skills = Column(Text, default="{}")
    inventory = Column(Text, default="{}")

