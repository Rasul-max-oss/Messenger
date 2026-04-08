import sqlite3
import os
from flask import Flask, render_template, request,redirect,url_for



app = Flask(__name__)

DATABASE = 'books_2.db'


def init_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            page INTEGER NOT NULL,
            img TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()



def get_book():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def book():
    db =get_book()
    books = db.execute('SELECT * FROM books ORDER BY id').fetchall()
    db.close()
    return render_template('books.html', books=books)


@app.route('/add_books',methods=['POST'])
def add_book():
    if request.method == 'POST':
        name = request.form.get('name')
        author = request.form.get('author')
        year = int(request.form.get('year'))
        page = int(request.form.get('page'))
        img = request.form.get('img')
        if name and author and year and page and img:
            db = get_book()
            db.execute('INSERT INTO books (name,author,year,page,img) VALUES (?,?,?,?,?)', (name,author,year,page,img))
            db.commit()
            db.close()
    return redirect(url_for('book'))




# DATABASE = 'cars.db'
#
# def init_db():
#     conn = sqlite3.connect(DATABASE)
#     conn.execute("""
#         CREATE TABLE IF NOT EXISTS cars (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             brand TEXT NOT NULL,
#             model TEXT NOT NULL,
#             color TEXT NOT NULL,
#             price INTEGER NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()
#
# def get_car():
#     conn = sqlite3.connect(DATABASE)
#     conn.row_factory = sqlite3.Row
#     return conn
#
# @app.route('/')
# def cars():
#     db=get_car()
#     cars = db.execute('SELECT * FROM cars ORDER BY id').fetchall()
#     db.close()
#     return render_template('cars.html', cars=cars)
#
# @app.route('/add_cars',methods=['POST'])
# def add_cars():
#     if request.method == 'POST':
#         brand = request.form.get('brand')
#         model = request.form.get('model')
#         color = request.form.get('color')
#         price = int(request.form.get('price'))
#         if brand and model and color and price:
#             db=get_car()
#             db.execute('INSERT INTO cars (brand,model,color,price) VALUES (?,?,?,?)',(brand,model,color,price))
#             db.commit()
#             db.close()
#
#     return redirect(url_for('cars'))



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
