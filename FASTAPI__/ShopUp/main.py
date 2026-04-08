import uvicorn
from fastapi import FastAPI, Depends, Form, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from starlette.responses import HTMLResponse

# 1. База данных
DB_URL = "sqlite:///./users1.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)



class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    password = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    price = Column(Float)
    count = Column(Integer)
    category = Column(String)
    img_url = Column(String)


class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer, default=1)



class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    number = Column(Integer)
    email = Column(String)
    adders = Column(String)



# СОЗДАЕМ ТАБЛИЦЫ (Важно!)
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def check_admin(request: Request, db: Session):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return None

    return db.query(Admin).filter(Admin.id == int(user_id)).first()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 2. Роуты (Страницы)
@app.get('/')
def get_reg(request: Request):
    return templates.TemplateResponse("reg.html", {"request": request})


@app.get('/login_page')
def get_login(request: Request):
    # Убрал / перед login.html
    return templates.TemplateResponse("login.html", {"request": request})

@app.get('/admin_page')
def get_admin(request: Request):
    return templates.TemplateResponse("admin.html",{"request": request})


@app.get('/profile')
def profile(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse('/login_page')

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        return RedirectResponse('/login_page')

    return templates.TemplateResponse("profile.html", {"request": request, "user": user})

@app.get('/add_product_page')
def get_add_product_page(request: Request,db: Session = Depends(get_db)):
    admin_id = request.cookies.get("admin_id")
    if not admin_id:
        return RedirectResponse('/admin_login')
    admin_user = db.query(Admin).filter(Admin.id ==int(admin_id)).first()
    if not admin_user:
        return RedirectResponse('/admin_login')

    return templates.TemplateResponse("add_product.html", {"request": request})

@app.get('/cart_page')
def cart_page(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse('/login_page')

    items = db.query(CartItem).filter(CartItem.user_id == int(user_id)).all()

    # делаем словарь продуктов
    products = {p.id: p for p in db.query(Product).all()}

    return templates.TemplateResponse("cart.html", {
        "request": request,
        "items": items,
        "products": products
    })


# 3. Логика (Action)
@app.post('/register')
def register(username: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == username).first():
        return "Такой логин занят"

    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()
    return RedirectResponse('/login_page', status_code=303)


@app.post('/login')
def login(username: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username, User.password == password).first()
    if not user:
        return "Неверный логин или пароль"

    response = RedirectResponse('/profile', status_code=303)
    response.set_cookie(key="user_id", value=str(user.id))
    return response

@app.post('/admin')
def admin(username: str = Form(),password: str = Form(), db: Session = Depends(get_db)):
    if username == "admin" and password == "123":
        admin_user = db.query(Admin).filter(Admin.username == "Admin").first()
        if not admin_user:
            admin_user = Admin(username= "Admin",password="123")
            db.add(admin_user)
            db.commit()
        response = RedirectResponse('/admin_panel',status_code=303)
        response.set_cookie(key="admin_id",value=str(admin_user.id))
        return response
    return "Неверный логин или пароль!"


@app.get('/admin_login')
def get_admin_login(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})

@app.get('/admin_panel')
def get_admin_panel(request: Request,db: Session = Depends(get_db)):
    #Проверяем авторизацию
    admin_id = request.cookies.get("admin_id")
    if not admin_id:
        return RedirectResponse('/admin_login')
    admin_user = db.query(Admin).filter(Admin.id == int(admin_id)).first()
    if not admin_user:
        return RedirectResponse('/admin_login')
    users = db.query(User).all()
    admins = db.query(Admin).all()
    products_count = db.query(Product).count()
    admins_count = db.query(Admin).count()
    users_count = db.query(User).count()
    items = db.query(CartItem).all()
    orders = db.query(Order).all()

    return templates.TemplateResponse("admin_panel.html",{"request": request,"products_count": products_count,"admins_count":admins_count,"users_count":users_count,"users": users,"admins":admins,"items": items, "orders":orders})

@app.get('/admin_logout')
def admin_logout():
    response = RedirectResponse('/products')
    response.delete_cookie("admin_id")
    return response

@app.get('/logout')
def logout():
    response = RedirectResponse('/login_page')
    response.delete_cookie("user_id")
    return response

@app.get('/products')
def show_all_products(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    if not products:
        return templates.TemplateResponse("all_products.html", {
            "request": request,
            "products": []
        })

    return templates.TemplateResponse("all_products.html", context={"request": request,"products": products})


@app.post('/add_product')
def add_product(
    db: Session = Depends(get_db),
    name: str = Form(),
    price: float = Form(),
    count: int = Form(),
    category: str = Form(),
    img_url: str = Form(default="")
):
    if not name or not category:
        return {"error": "Заполни поля"}

    exsist_product = db.query(Product).filter(
        Product.name == name,
        Product.category == category
    ).first()

    if exsist_product:
        exsist_product.count += count
        db.commit()
        return RedirectResponse("/products", status_code=303)

    new_product = Product(
        name=name,
        price=price,
        count=count,
        category=category,
        img_url=img_url
    )

    db.add(new_product)
    db.commit()

    return RedirectResponse("/products", status_code=303)





@app.post('/add_to_cart')
async def add_to_cart(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse('/login_page', status_code=303)

    form_data = await request.form()
    product_id = int(form_data.get("product_id"))

    cart_item = db.query(CartItem).filter(
        CartItem.user_id == int(user_id),
        CartItem.product_id == product_id
    ).first()

    if cart_item:
        cart_item.quantity += 1
    else:
        new_cart_item = CartItem(user_id=int(user_id), product_id=product_id, quantity=1)
        db.add(new_cart_item)

    db.commit()

    return RedirectResponse('/cart_page', status_code=303)

@app.post('/remove_from_cart')
async def remove_from_cart(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    item_id = form_data.get("item_id")  # Получаем ID записи в корзине
    if not item_id:
        return RedirectResponse('/cart_page', status_code=303)


    if item_id:
        cart_item = db.query(CartItem).filter(CartItem.id == int(item_id)).first()
        if cart_item:
            db.delete(cart_item)
            db.commit()

    return RedirectResponse('/cart_page', status_code=303)

@app.get('/order_page')
def order_page(request: Request,db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse('/login_page', status_code=303)
    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        return RedirectResponse('/login_page', status_code=303)

    return templates.TemplateResponse("order.html",{"request": request})

@app.post('/order')
def order(name: str = Form(), number: int = Form(), email: str = Form(), adders: str = Form(),  db: Session = Depends(get_db)):
    if not name or not number or not email or not adders:
        return RedirectResponse('/order_page')

    new_order = Order(
        name= name,
        number = number,
        email=email,
        adders=adders
    )
    db.add(new_order)
    db.commit()

    return RedirectResponse('/products', status_code=303)



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

