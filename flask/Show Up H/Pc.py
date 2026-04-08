
from ShowUp.models import Order
from server import db,computer
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)

#НАСТРОЙКА БД
#Если у вас другая бд то меняем shop.db на другое название
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Замени в продакшене!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'shop10.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Создаём папку instance, если её нет. Это папка для DB
os.makedirs(app.instance_path, exist_ok=True)
db.init_app(app)




# Флаг для инициализации БД один раз
_initialized = False


@app.before_request
def init_app():
    global _initialized
    if 'Computer' not in session:
        session['Computer'] = []
    if not _initialized:
        with app.app_context():
            db.create_all()
            if computer.query.count() == 0:
                demo_products = [
                    computer(name="ASUS",ram=16,processor="AMD Ryzen Threadripper PRO 9995WX",video_card="RTX 4090 Ti",ssd=2048,price=100500),
                    computer(name="ASUS",ram=16,processor="AMD Ryzen Threadripper PRO 5000WX",video_card="RTX 4070 Ti",ssd=1024,price=80000),
                    computer(name="ASUS",ram=16,processor="AMD Ryzen Apple Pro max air galaxy 20",video_card="RTX 3090 Ti",ssd=512,price=60000)
                ]
                for p in demo_products:
                    db.session.add(p)
                db.session.commit()

        _initialized = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

@app.route('/')
def show_computers():
    computers = computer.query.all()
    return render_template('shop_computers.html',computers=computers)

@app.route('/admin/login',methods=['GET','POST'])
def admin_log():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash('Вы вошли как администратор!', 'success')
            return redirect(url_for('admin_add'))
        else:
            flash('Неверный пароль или логин!', 'error')
    return render_template('Login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in',None)
    flash('Вы вышли из админ аккаунта!','info')
    return redirect(url_for('show_computers'))

@app.route('/admin/add',methods=['GET','POST'])
def admin_add():
    if not session.get('admin_logged_in'):
        flash('Пожалуйста, войдите как администратор!', 'error')
        return redirect(url_for('admin_login'))
    if request.method == 'POST':
        name = request.form['name']
        ram = request.form['ram']
        processor = request.form['processor']
        video_card = request.form['video_card']
        ssd = request.form['ssd']
        price = float(request.form['price'])
        img = request.form['img']

        items = computer(name=name,ram=ram,processor=processor,video_card=video_card,ssd=ssd,price=price,img = img)
        db.session.add(items)
        db.session.commit()
        flash(f'Товар {name} успешно добавлен', 'success')
        return redirect(url_for('show_computers'))
    return render_template('add.html')

@app.route('/add_to_cart/<int:computer_id>')
def add_to_cart(computer_id):
    items = computer.query.get_or_404(computer_id)
    cart = session['cart']
    cart.append(computer_id)
    session['cart'] = cart
    flash(f"{computer.name} добавлен в корзину!", 'success')
    return redirect(url_for('show_computers'))

@app.route('/cart')
def cart():
    cart_ids = session.get('cart',[])
    if cart_ids:
        computers = computer.query.filter(computer.id.in_(cart_ids)).all()
        total = sum(p.price for p in computers)
    else:
        computers = []
        total = 0
    return render_template('cart.html',computers = computers,total=total)

@app.route('/checkout',methods=['POST','GET'])
def checkout():
    cart_ids = session.get('cart',[])
    if not cart_ids:
        flash('У вас пустая корзинка, добавьте вещей!','error')
        return redirect(url_for('cart'))
    computers = computer.query.filter(computer.id.in_(cart_ids)).all()
    total = sum(p.price for p in computers)

    if request.method == 'POST':
        name = request.form.get('name').strip()
        address = request.form.get('address').strip()
        phone = request.form.get('phone').strip()
        if not name and address and phone:
            flash('Пожалуйста, заполните все поля.', 'error')
            return render_template('checkout.html', computers=computers, total=total)
        order = Order(
            customer_name = name,
            address = address,
            phone = phone,
            total = total
        )
        db.session.add(order)
        db.session.commit()

        session['cart'] = []
        flash('Заказ успешно оформлен! Спасибо за покупку.', 'success')
        return redirect(url_for('show_computers'))
    return render_template('checkout.html',computers=computers,total=total)

@app.route('/admin/orders')
def admin_orders():
    if not session.get('admin_logged_in'):
        flash('Пожалуйста войдите как админ!')
        return redirect(url_for('admin_login'))

    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin_orders.html', orders=orders)







if __name__ == '__main__':
    app.run(debug=True)





