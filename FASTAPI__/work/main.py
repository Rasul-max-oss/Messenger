from typing import Dict, Optional, List, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from models import Task,SessionLocal,engine
from sqlalchemy.orm import session

Task.metadata.create_all(bind=engine)

app = FastAPI()

class Todolist(BaseModel):
    title: str
    description: str
    is_completed: bool

@app.post("/todo_list")
def add_task(t: Todolist):
    db = SessionLocal()

    db_task = Task(title=t.title,description=t.description,is_completed=t.is_completed)

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()

    return {"id": db_task.id,"Title": db_task.title,"description": db_task.description,"is_completed":db_task.is_completed}


@app.get('/tasks')
def get_all():
    db=SessionLocal()
    tasks = db.query(Task).all()
    db.close()

    return tasks

@app.get('/tasks/{task_id}')
def get_by_id(id:int):
    db = SessionLocal()

    get_info = db.query(Task).filter(Task.id == id).first()
    db.close()

    if get_info is None:
        raise HTTPException(status_code=404,detail="Not found")

    return get_info

@app.get('/tasks/name/{task_name}')
def get_by_name(name:str):
    db = SessionLocal()

    get_info = db.query(Task).filter(Task.title == name).first()
    db.close()

    if get_info is None:
        raise HTTPException(status_code=404,detail="Not found")

    return get_info

class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool


@app.put('/tasks/{task_id}')
def update(id:int,tu:TaskUpdate):
    db =SessionLocal()

    get_info = db.query(Task).filter(Task.id == id).first()

    if not get_info:
        db.close()
        raise HTTPException(status_code=404, detail="Задача не найдена")
    if tu.title:
        get_info.title = tu.title
    if tu.description:
        get_info.description = tu.description
    if tu.is_completed:
        get_info.is_completed = tu.is_completed

    db.commit()
    db.refresh(get_info)
    db.close()

    return {"Id": id,"title":get_info.title,"description":get_info.description,"is_completed":get_info.is_completed}


@app.delete('/tasks/{task_id}')
def delet_task(id:int):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(task)
    db.commit()
    db.close()

    return {"Msg": "Удалено!"}








