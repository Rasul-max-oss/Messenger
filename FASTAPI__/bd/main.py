# pip install fastapi uvicorn pydantic

import sqlite3
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

# 🚀 FastAPI
app = FastAPI(title="Books API")

# 🗄️ База данных
def get_db():
    conn = sqlite3.connect("book_2.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        author TEXT NOT NULL,
        year INTEGER,
        genre TEXT,
        pages INTEGER,
        status TEXT NOT NULL,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


create_tables()

# 📋 Модели
class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    genre: Optional[str] = None
    pages: Optional[int] = None
    status: str


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int]
    genre: Optional[str]
    pages: Optional[int]
    status: str
    created_at: str


class BookUpdate(BaseModel):
    year: Optional[int] = None
    genre: Optional[str] = None
    pages: Optional[int] = None
    status: Optional[str] = None


# 🏠 Главная
@app.get("/")
def root():
    return {"message": "Books API работает 📚"}


# ➕ Добавить книгу
@app.post("/books/", response_model=BookResponse)
def add_book(book: BookCreate):
    conn = get_db()
    cursor = conn.cursor()

    try:
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
        INSERT INTO books(title,author,year,genre,pages,status,created_at)
        VALUES(?,?,?,?,?,?,?)
        """, (
            book.title,
            book.author,
            book.year,
            book.genre,
            book.pages,
            book.status,
            created_at
        ))

        conn.commit()

        cursor.execute("SELECT * FROM books WHERE id=?", (cursor.lastrowid,))
        new_book = cursor.fetchone()

        return dict(new_book)

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Книга с таким названием уже существует"
        )
    finally:
        conn.close()


# 📚 Получить список книг (с фильтрами)
@app.get("/books/", response_model=List[BookResponse])
def get_books(
        author: Optional[str] = None,
        genre: Optional[str] = None,
        status: Optional[str] = None
):
    conn = get_db()
    cursor = conn.cursor()

    query = "SELECT * FROM books WHERE 1=1"
    params = []

    if author:
        query += " AND author=?"
        params.append(author)

    if genre:
        query += " AND genre=?"
        params.append(genre)

    if status:
        query += " AND status=?"
        params.append(status)

    cursor.execute(query, params)
    books = cursor.fetchall()
    conn.close()

    return [dict(book) for book in books]


# 🔎 Получить книгу по ID
@app.get("/books/{book_id}", response_model=BookResponse)
def get_book_by_id(book_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()
    conn.close()

    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return dict(book)


# ✏️ Обновить книгу
@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    exists = cursor.fetchone()

    if exists is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Книга не найдена")

    fields = []
    values = []

    if book.year is not None:
        fields.append("year=?")
        values.append(book.year)

    if book.genre is not None:
        fields.append("genre=?")
        values.append(book.genre)

    if book.pages is not None:
        fields.append("pages=?")
        values.append(book.pages)

    if book.status is not None:
        fields.append("status=?")
        values.append(book.status)

    if not fields:
        conn.close()
        raise HTTPException(status_code=400, detail="Нет данных для обновления")

    query = f"UPDATE books SET {', '.join(fields)} WHERE id=?"
    values.append(book_id)

    cursor.execute(query, values)
    conn.commit()

    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    updated_book = cursor.fetchone()
    conn.close()

    return dict(updated_book)


# ❌ Удалить книгу
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM books WHERE id=?", (book_id,))
    exists = cursor.fetchone()

    if exists is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Книга не найдена")

    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

    return {"message": f"Книга {book_id} удалена"}


# ▶️ Запуск
if __name__ == "__main__":
    import uvicorn
    print("🌐 http://127.0.0.1:8000")
    print("📚 http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)
