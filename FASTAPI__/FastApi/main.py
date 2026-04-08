from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = []

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(message: str):
    tasks.append(message)
    return {"status": "added"}

@app.delete("/tasks")
def delete_task(message: str):
    if message in tasks:
        tasks.remove(message)
        return {"status": "deleted"}
    return {"status": "not found"}

@app.put("/tasks")
def edit_task(old: str, new: str):
    if old in tasks:
        i = tasks.index(old)
        tasks[i] = new
        return {"status": "updated"}
    return {"status": "not found"}
