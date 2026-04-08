import sqlite3
import os
from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

DATABASE = 'users.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    db=get_db()
    users = db.execute('SELECT * FROM users ORDER BY id').fetchall()
    db.close()
    return render_template('index.html',users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name').strip()
        email = request.form.get('email').strip()
        if name and email:
            db=get_db()
            db.execute('INSERT INTO users (name,email) VALUES (?,?)',(name,email))
            db.commit()
            db.close()

    return redirect(url_for('index'))





if __name__ == '__main__':
    init_db()
    app.run(debug=True)

























