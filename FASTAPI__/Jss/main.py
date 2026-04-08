from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uuid
import os

app = FastAPI(title="Contacts App")


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Модель контакта
class Contact(BaseModel):
    id: str
    name: str
    phone: str
    email: str
    address: Optional[str] = ""


# "База данных"
contacts_db: List[Contact] = [
    Contact(id=str(uuid.uuid4()), name="Иван Петров", phone="+7 999 123-45-67", email="ivan@mail.com", address="Москва"),
    Contact(id=str(uuid.uuid4()), name="Мария Сидорова", phone="+7 999 765-43-21", email="maria@mail.com", address="СПб"),
]


# Главная страница
@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


# Все контакты
@app.get("/api/contacts", response_model=List[Contact])
async def get_contacts():
    return contacts_db


# Один контакт
@app.get("/api/contacts/{contact_id}", response_model=Contact)
async def get_contact(contact_id: str):
    for contact in contacts_db:
        if contact.id == contact_id:
            return contact
    raise HTTPException(status_code=404, detail="Contact not found")


# Поиск
@app.get("/api/contacts/search")
async def search_contacts(q: str = ""):

    if not q:
        return contacts_db

    q = q.lower()

    return [
        c for c in contacts_db
        if q in c.name.lower()
        or q in c.phone.lower()
        or q in c.email.lower()
    ]


# Добавить
@app.post("/api/contacts", response_model=Contact)
async def create_contact(
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    address: str = Form("")
):

    new_contact = Contact(
        id=str(uuid.uuid4()),
        name=name,
        phone=phone,
        email=email,
        address=address
    )

    contacts_db.append(new_contact)

    return new_contact


# Обновить
@app.get("/api/contacts/{contact_id}")
async def update_contact(
    contact_id: str,
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    address: str = Form("")
):

    for i, contact in enumerate(contacts_db):

        if contact.id == contact_id:

            contacts_db[i] = Contact(
                id=contact_id,
                name=name,
                phone=phone,
                email=email,
                address=address
            )

            return contacts_db[i]

    raise HTTPException(status_code=404, detail="Contact not found")


# Удалить
@app.delete("/api/contacts/{contact_id}")
async def delete_contact(contact_id: str):

    for i, contact in enumerate(contacts_db):

        if contact.id == contact_id:

            contacts_db.pop(i)

            return {"message": "deleted"}

    raise HTTPException(status_code=404, detail="Contact not found")


# Запуск
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )