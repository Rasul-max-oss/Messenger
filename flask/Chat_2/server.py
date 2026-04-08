from flask import Flask, request, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from model import db, User, Message
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-for-testing-only'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        if not username and password:
            flash('Заполните все ячейки!')
        if User.query.filter_by(username=username).first():
            flash('Пользователь уже существует!')
            return render_template('register.html')
        hash_ps = generate_password_hash(password)
        new_user = User(username=username,password=hash_ps)
        db.session.add(new_user)
        db.session.commit()
        flash("Регистрация успешна!")
        return redirect(url_for('forum'))
    return render_template('register.html',user=new_user)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password,password):
            session['user_id'] = user.id
            flash(f'Шалом, {username}')
            return redirect(url_for('forum'))
        else:
            flash('Неверное имя или пароль!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    flash('Молодой чебурек, вы вышли!')
    return render_template('login.html')

@app.route('/',methods=['GET','POST'])
def forum():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    user = User.query.get(user_id)
    if not user:
        session.pop('user_id',None)
        return redirect(url_for('login'))
    if request.method == 'POST':
        content = request.form.get('content',).strip()
        if content:
            msg = Message(content=content,user_id=user.id)
            db.session.add(msg)
            db.session.commit()
        return redirect(url_for('forum'))
    messages = Message.query.order_by(Message.timestamp).limit(50).all()
    return render_template('Forum.html',user=user,messages=messages)

@app.route('/delete_message/<int:message_id>',methods=['POST'])
def delete_message(message_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    message = Message.query.get(message_id)
    if message.user_id != user_id:
        return redirect(url_for('forum'))
    db.session.delete(message)
    db.session.commit()
    flash('Сообщение удалено!')
    return redirect(url_for('forum'))

@app.route('/edit_message/<int:message_id>', methods=['GET', 'POST'])
def edit_message(message_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    message = Message.query.get(message_id)
    if not message or message.user_id != user_id:
        return redirect(url_for('forum'))

    if request.method == 'POST':
        new_content = request.form.get('content', '').strip()
        if not new_content:
            flash('Сообщение не может быть пустым!')
        else:
            message.content = new_content
            db.session.commit()
            flash('Сообщение обновлено!')
        return redirect(url_for('forum'))

    # ← ОБЯЗАТЕЛЬНО: передаём editing_message
    return render_template(
        'Forum.html',
        user=User.query.get(user_id),
        messages=Message.query.order_by(Message.timestamp).limit(50).all(),
        editing_message=message
    )

@app.route('/color_message/<int:message_id>', methods=['GET', 'POST'])
def color_message(message_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    message = Message.query.get(message_id)
    if not message or message.user_id != user_id:
        return redirect(url_for('forum'))

    if request.method == 'POST':
        new_color = request.form.get("color")
        if new_color:
            message.message_color = new_color
            db.session.commit()
        return redirect(url_for('forum'))

    return render_template("color_message.html", message=message)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)