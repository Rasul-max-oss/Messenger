import os
import sqlite3
from math import expm1
from flask import Flask, render_template, request, redirect, url_for, flash, session



app = Flask(__name__)

DATABASE = 'users.db'

app.secret_key = 'your-secret-key-change-in-production'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)

init_db()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password']
        if not (username and email and password):
            flash('Вск поля обязательные.')
            return render_template('register_chat')
        from werkzeug.security import generate_password_hash
        password_hash = generate_password_hash(password)
        try:
            with get_db_connection() as conn:
                conn.execute('INSERT INTO chats (username,email,password_hash) VALUES (?,?,?)',(username,email,password_hash))
            flash('Регистрация успешна! теперь войдите.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Имя пользователя или email уже заняты.')
    return render_template('register_chat.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with get_db_connection() as conn:
            user = conn.execute('SELECT * FROM chats WHERE username = ?',(username,)).fetchone()
            if user:
                from werkzeug.security import check_password_hash
                if check_password_hash(user['password_hash'],password):
                    session['user_id'] = user['id']
                    session['username'] = user['username']
                    return redirect(url_for('profile'))
                flash('Неверное имя пользователь или пароль')
    return render_template('Log_chat.html')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Profil_Chat.html',username =session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# @app.route('/')
# def index():
#     return redirect(url_for('login'))
#
# @app.route('/register',methods=['GET','POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username'].strip()
#         email = request.form['email'].strip()
#         password = request.form['password']
#         if not (username and email and password):
#             flash('Все поля обязательные.')
#             return render_template('reg.html')
#         from werkzeug.security import generate_password_hash
#         password_hash = generate_password_hash(password)
#         try:
#             with get_db_connection() as conn:
#                 conn.execute('INSERT INTO users (username,email,password_hash) VALUES (?,?,?)',
#                              (username,email,password_hash)
#                         )
#                 flash('Регистрация успешна! Теперь войдите.')
#                 return redirect(url_for('login'))
#         except sqlite3.IntegrityError:
#             flash('Имя пользователя или email уже заняты.')
#     return render_template('register.html')
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         with get_db_connection() as conn:
#             user = conn.execute('SELECT * FROM users WHERE username = ?',(username,)).fetchall()
#             if user:
#                 from werkzeug.security import check_password_hash
#                 if check_password_hash(user['password_hash'],password):
#                     session['user_id'] = user['id']
#                     session['username'] = user['username']
#                     return redirect(url_for('profile'))
#             flash('Неверное имя пользователь или пароль')
#         return render_template('login.html')
#
# @app.route('/profile')
# def profile():
#     if 'user_id' not in session:
#         return redirect(url_for('login'))
#     return render_template('profile.html',username=session['username'])
#
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('login'))
#





if __name__ == '__main__':
    app.run(debug=True)