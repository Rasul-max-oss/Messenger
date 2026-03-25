import uvicorn
from fastapi import FastAPI, Depends, Form, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from starlette.responses import HTMLResponse

# 1. База данных
DB_URL = "sqlite:///./users.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id=Column(Integer,primary_key=True,index=True)
    username = Column(String)
    number = Column(Integer,unique=True)
    adders = Column(String)
    avatar = Column(String)
    
class Chat(Base):
    """Чат (беседа между двумя пользователями)"""
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    user1_id = Column(Integer, ForeignKey("users.id"))  # создатель
    user2_id = Column(Integer, ForeignKey("users.id"))  # собеседник


class Message(Base):
    """Сообщение в чате"""
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String)
    timestamp = Column(String)


Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/register_page')
def register_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post('/register')
def register(
    username: str = Form(...),
    number: int = Form(...),
    adders: str = Form(...),
    db: Session = Depends(get_db)
):
    # Проверка, существует ли пользователь с таким номером
    existing = db.query(User).filter(User.number == number).first()
    if existing:
        return {"error": "Пользователь с таким номером уже существует"}
    
    # Создание нового пользователя
    new_user = User(
        username=username,
        number=number,
        adders=adders,
        avatar="/static/default_avatar.png"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return RedirectResponse(url="/login_page", status_code=303)










