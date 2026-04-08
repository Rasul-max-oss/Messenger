from typing import Dict, Optional, List, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from models import User,SessionLocal,engine
from sqlalchemy.orm import session
import json


User.metadata.create_all(bind=engine)

app = FastAPI()


# Pydantic модель - как данные приходят из запроса
class UserSchema(BaseModel):
    name: str
    age: int


@app.post('/add')
def add_user(user: UserSchema):  # FastAPI автоматически валидирует JSON по Pydantic модели
    # Открываем сессию БД
    db = SessionLocal()

    # Создаём SQLAlchemy объект из Pydantic данных
    db_user = User(name=user.name, age=user.age)

    # Сохраняем в БД
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # забираем из БД (особенно id)
    db.close()

    # Возвращаем JSON
    return {"id": db_user.id, "name": db_user.name, "age": db_user.age}


@app.get('/users')
def get_users():
    db = SessionLocal()
    users = db.query(User).all()  # SQL: SELECT * FROM users
    db.close()
    return users


@app.get('/users/{user_id}')
def find_by_id(user_id: int):
    db = SessionLocal()

    db_user = db.query(User).filter(User.id == user_id).first()
    db.close()

    if db_user is None:
        raise HTTPException(status_code=404,detail="Not found")

    return {"id": db_user.id,"name":db_user.name,"age":db_user.age}

@app.get('/user/name/{user_name}')
def find_by_name(user_name: str):
    db = SessionLocal()

    user = db.query(User).filter(User.name == user_name).first()
    db.close()

    if user is None:
        raise HTTPException(status_code=404, detail="Not found")

    return {"id": user.id, "name": user.name, "age": user.age}

@app.delete('/user/{user_id}')
def delete(user_id: int):
    db = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(user)
    db.commit()
    db.close()

    return {"Msg": "Успешно"}


class UserUpdateSchema(BaseModel):
    name: str
    age: int


@app.put('/user/{user_id}')
def update_user(user_id: int,user_data:UserUpdateSchema):
    db = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        db.close()
        raise HTTPException(status_code=404,detail="Пользователь не найден")
    if user_data.name is not None:
        user.name = user_data.name
    if user_data.age is not None:
        user.age = user_data.age

    db.commit()
    db.refresh(user)
    db.close()

    return {"id": user.id,"name": user.name, 'age': user.age}


if __name__ == "__main__":
    import uvicorn
    print("🌐 http://127.0.0.1:8000")
    print("📚 http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)










