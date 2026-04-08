from typing import List

from click.core import batch
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import SQLORMExpression

app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int
#     is_student: bool
#
# @app.post('/')
# def check(user: User):
#     return {
#         "Сообщение": f"Привет, {user.name}",
#         "Информация": f"Тебе {user.age} лет, студент: {user.is_student}"
#     }

# class Toy(BaseModel):
#     name: str
#     price: float
#     age_rating: int
#
# @app.post('/')
# def add_toys(product: Toy):
#     return {
#         "Игрушка": f"Название: {product.name}",
#         "Информация": f"Ограничение по возросту {product.age_rating}+, Цена: {product.price}"
#     }
#
#
#
# class Store(BaseModel):
#     store_id: int
#     name: str
#     toys: List[Toy] = []
#
# @app.post('/toys')
# def store_name(store: Store):
#     sum_toys = len(store.toys)
#     sum_price = sum(toy.price for toy in store.toys)
#     return {
#         "store_name": f"Название магазина: {store.name}",
#         "Сумма": f"Сумма всех игрушек: {sum_price}",
#         "Количество": f"Количество всех игрушек: {sum_toys}"
#     }
#
#
# class Purchase(BaseModel):
#     buyer_name: str
#     toy_name: str
#     quantity: int
#     discount_code: str
#
# @app.post('/buy')
# def libery(purchase: Purchase):
#     if purchase.quantity > 0 and purchase.discount_code == 'KIDS10':
#         return {
#             "Buyer": f"Имя: {purchase.buyer_name}",
#             "toy": f"Название игрушки {purchase.toy_name}",
#             "quantity": f"Количество {purchase.quantity}",
#             "discount_applied": "применена ли скидка"
#         }
#     else:
#         return {
#             "Ошибка": "Что-то не верное!"
#         }

class Book(BaseModel):
    title: str
    author: str
    year: int
    pages: int

@app.post('/book')
def show_book(book: Book):
    return {
        "Title and Author": f"Название: {book.title}, Создатель: {book.author}",
        "Year and Pages": f"Год выпуска: {book.year}, количество страниц: {book.pages}"
    }

class Library(BaseModel):
    library_id: int
    name: str
    books: List[Book] = []

@app.post('/libraries')
def show_libraries(library: Library):
    sum_books = sum(book.pages for book in library.books)
    return {
        "library_id": f"{library.library_id}",
        "name": f"Название: {library.name}",
        "books": f"Все книги: {library.books}",
        "Страницы": f"Общее количество страниц: {sum_books}"
    }

class Reader(BaseModel):
    reader_id: int
    name: str
    age: int
    favorite_genres: str
    books_borrowed: List[Book] = []

@app.post('/reader')
def show_reader(reader: Reader):
    book = Book()
    if reader.age <= 6:
        return {"Ошибка": "Ваш реальный возраст меньше 6 лет!"}
    if reader.age <= 16 and book.year <= 2001:
        return {"Ошибка": "Ограничения по возрасту!"}

    book_list = len(reader.books_borrowed)
    if book_list >= 5:
        return {"Ошибка": "Лимит по взятию книг!"}

    return {
        "Name and Age and Id": f"Id: {reader.reader_id}, Имя: {reader.name}, Возраст: {reader.age}",
        "Gener": f"Ваш любимый жанр: {reader.favorite_genres}",
        "List's books": f"Список книг: {reader.books_borrowed}"
    }
    




