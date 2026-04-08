# class Person:
#     def __init__(self,name,dateryear,age,hobby):
#         self.name = name
#         self.dateryear = dateryear
#         self.age = age
#         self.hobby = hobby
#
#     def info(self):
#         print(f"Имя: {self.name}")
#         print(f"Дата рождение:{self.dateryear}")
#         print(f"Возраст: {self.age}")
#         print(f"Хобби: {self.hobby}")
#
#     def move(self):
#         print(f"{self.name} ходит...")
#
#     def eat(self):
#         print(f"{self.name} ест...")
#
# # person1 = Person("Алекс", "15.06.2001",23,"Баскетбол")
# # person1.info()
# # person1.move()
# # person1.eat()
#
# person2 = Person("Вася","15.03.2011",13,"Футбол")
# person2.info()
# person2.eat()
# person2.move()



# class Car:
#     def __init__(self,age,model,speed,pts,km):
#         self.age = age
#         self.model = model
#         self.speed = speed
#         self.pts = pts
#         self.km = km
#
#     def info(self):
#         print(f"Возраст машины: {self.age}")
#         print(f"Модель машины: {self.model}")
#         print(f"Макс. скорость у машины: {self.speed}")
#         print(f"Птс машины: {self.pts}")
#         print(f"Пробег машины: {self.km}")
#
#     def on(self):
#         for i in range(10):
#             print("Двигатель заводится", i * ".")
#     def off(self):
#        print("Двигатель отключен")
#
# car1 = Car(10,"Toyota",200,"3 человока","150000km" )
# car1.info()
# car1.on()

# class Pc:
#     def __init__(self,on,ram,ssd,videocard,rgb,cold):
#         self.on = on
#         self.ram = ram
#         self.ssd = ssd
#         self.videocard = videocard
#         self.rgb = rgb
#         self.cold = cold
#
#     def on_conrol(self):
#         if self.on:
#             print("Компютор и так включен")
#         else:
#             print("Включение компютора")
#             self.on = True
#     def off_conrol(self):
#         if self.on == False:
#             print("Компютор и так выключен")
#         else:
#             print("Выключение компютора")
#             self.on = False
#
# pc1 = Pc(True, 16,"2gb", "5090Ti","is","is")
# pc1.off_conrol()
# pc1.off_conrol()

# class Book:
#     def __init__(self,title,author,year,genre):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.genre = genre
#
#     def info(self):
#         print(f"Имя книги: {self.title}")
#         print(f"Автор книги: {self.author}")
#         print(f"Жанар книги: {self.genre}")
#         print(f"Год выпуска книги: {self.year}")
#
#     def year(self):
#         if self.year > 60:
#             print("Книги больше 60 лет!")
#         else:
#             print("Книги не настоль староя")
#
# book1 = Book("Гарри Поттер","Джоулинг роулинг",2000,"Фантастика")
# book1.info()
# book1.year()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Привет меня зовут {self.name} и мне {self.age} лет!")
#
#     def birtday(self):
#         self.age += 1
#         print(f"У меня сегодня день рождение, мне исполнелась {self.age}")
#
# person1 = Person("Петя",14)
# person1.info()
# person1.birtday()
# person1.info()

# class BankAccount:
#     def __init__(self,account_number,name,balance = 0):
#         self.account_number = account_number
#         self.name = name
#         self.balance = balance
#
#     def deposit(self,amount):
#         if amount >= 0:
#             self.balance += amount
#             print(f"Счет пополнен на {amount}. Текущий баланс: {self.balance}")
#         else:
#             print("Ошибка: сума должна бвть положительной")
#
#     def withdraw(self,amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"снята {amount}. Текущий баланс: {self.balance}")
#         else:
#             print("Ошибка: у вас недостаточно средств на счету")
#     def getbalance(self):
#         print(f"Текущий баланс: {self.balance}")
#
# # bank = BankAccount(100, "Jorge_Washington",15000)
# # bank.getbalance()
# # bank.deposit(200)
# # bank.withdraw(10000)
#
# print("=== Создание счета ===")
# account_number = input("Введите номер счета:")
# owner_name = input("Введите ИФО владельца: ")
# initial_balance = float(input("Введите начальный баланс: "))
# password = input("Создайте пароль для входа в счет: ")
# secret_word = input("Придумайте секретное слова если вы забудете пароль: ")
#
# bank = BankAccount(account_number,owner_name,initial_balance)
#
# def get_in(bank):
#     while True:
#         print("\n=== Меню ===")
#         print("1. Пополнить баланс")
#         print("2. Снять средства")
#         print("3. Проверить баланс")
#         print("4. Выйти")
#
#         user_choice = input("Выберите действие 1/2/3/4: ")
#         if user_choice == "1":
#             amount = float(input("Введите сумму для пополнение:"))
#             bank.deposit(amount)
#         if user_choice == "2":
#             amount = float(input("Введите сумму для снятие:"))
#             bank.withdraw(amount)
#         if user_choice == "3":
#             bank.getbalance()
#         if user_choice == "4":
#             print("До свидание(нет!)")
#             break
# while True:
#     print("1. Войти в аккаунт")
#     print("2. Выход")
#
#     user_choice = input("выберите команду 1/2:")
#     if user_choice == "1":
#         password_get = input("Введите пароль: ")
#         if password_get == password:
#             print("Вы вошли в аккаунт")
#             get_in(bank)
#         else:
#             user_choice = input("Введите секретное слово, вы забыли пароль:")
#             if user_choice == secret_word:
#                 get_in(bank)
#             else:
#                 print("Пока")
#                 break
#     if user_choice == "2":
#         break

# import time
#
# class Point:
#     def __init__(self,id, name, point):
#         print("==== Регистрация студента ====")
#         self.id = id
#         self.name = name
#         self.point = point
#
#     def addpoint(self,amount):
#         if amount >= 0:
#             self.point += amount
#             print(f"Текущий балл {self.point}")
#         else:
#             print("Ошибка: не может быть баланса меньше ноля!")
#
#     def withdraw(self,amount):
#         if 0 < amount <= self.point:
#             self.point -= amount
#             print(f"Текущий балл:{amount}")
#         else:
#             print(f"Вы не имеете нужное количество баллов. Текущий балл:{amount}")
#
#     def infobal(self):
#         print(self.name, "приветствую, тукущий балл:", self.point)
#
#     def nonrp(self, new_name):
#         self.name = new_name
#         print(f"Имя успешно изменино на: {new_name}")
#
# id = input("Введите свой ID студента:")
# name = input("Введите свое имя:")
# point = int(input("Введите количество очков которое хотите прибавить:"))
#
# student = Point(id, name, point)
#
# while True:
#     print("\n=== Меню ===")
#     print("1. Добавить баллы")
#     print("2. Списать баллы")
#     print("3. Проверить баллы")
#     print("4. Изменить имя студента")
#     print("5. Выйти")
#
#     user_choice = input("Выберите команду 1/2/3/4/5/6: ")
#     if user_choice == "1":
#         amount = int(input("Сколько баллов хотите добавить:"))
#         student.addpoint(amount)
#         print("Баллы успешно добавлены!")
#
#     if user_choice == "2":
#         amount = int(input("Сколько баллов хотите списать:"))
#         student.withdraw(amount)
#         print("Баллы успешно сняты")
#
#     if user_choice == "3":
#         student.infobal()
#         time.sleep(3)
#
#     if user_choice == "4":
#         student.nonrp()
#
#     if user_choice == "5":
#         print("До свидание")
#         break

#

# import time
#
# class Player:
#     def __init__(self,name):
#         self.name = name
#         self.health = 100
#
#     def move(self):
#         print(f"{self.name} идёт вперёд.")
#
#     def take_damage(self,damage):
#         self.health -= damage
#         print(f"{self.name} получил {damage} урона")
#         if self.health <= 0:
#             print(f"{self.name} погиб!")
#
#     def run(self):
#         print(f"{self.name} бежит назад")
#
#     def scary(self):
#         print(f"{self.name} бойтся. по нему стреляют")
#
#     def lay(self,target):
#         print(f"{self.name} упал на пол. его подстрелил {target.name}")
#
#
# class Cop(Player):
#     def __init__(self,name):
#         super().__init__(name)
#         self.gun = "Пистолет"
#
#     def shoot(self,target):
#         print(f"{self.name}  стреляет из {self.gun} по {target.name}!")
#         target.take_damage(20)
#
#     def arrest(self,target):
#         print(f"{self.name} арестовал(-a) {target.name}!")
#
#     def putin(self,target):
#         print(f"{self.name} садит в машину {target.name}")
#
# class Bandit(Player):
#     def __init__(self, name):
#         super().__init__(name)
#         self.gun = "Ак - 47"
#
#     def shoot(self,target):
#         print(f"{self.name}  стреляет из {self.gun} по {target.name}!")
#         target.take_damage(35)
#
#     def rob(self):
#         print(f"{self.name} грабит банк...")
#
#     def away(self):
#         print(f"{self.name} пытается вырвотся")
#
#     def gotit(self, target):
#         print(f"{self.name} спешно сбжал от {target.name}")
#
# class Businessman(Player):
#     def work(self):
#         print(f"{self.name} кправляет бизнесменом.")
#
#     def pay_taxes(self):
#         print(f"{self.name} платит налог в город.")
#
#     def buy(self):
#         print(f"{self.name} купил новый бизнес!")
#
#     def sell(self):
#         print(f"{self.name} успешно продал свой бизнес за 10.000.000 долорав")
#
# class Worker(Player):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def give(self, target):
#         print(f"{self.name} дает деньги {target.name}")
#
#     def layr(self,target):
#         print(f"{self.name} пригнулся (-ь) напал. в низ стреляет {target.name}")
#
# # === Game starts here ===
# print("=== Добро пожаловать в текстовую RPG в стиле SAMP RP ===")
# time.sleep(2)  # Пауза перед началом
#
#
#
# offcer = Cop("Офицер Рик")
#
# criminal = Bandit("Взрывной Вася")
#
# boss = Businessman("Босс Джон")
#
# player1 = Player("вася")
#
# player2 = Player("петя")
#
# worker = Worker("люда")
#
# for i in range(3):
#     print(f"\n --- Раунд {i + 1} ---")
#     offcer.move()
#     time.sleep(2)
#
#     player1.move()
#     time.sleep(2)
#
#     player2.move()
#     time.sleep(2)
#
#     criminal.move()
#     time.sleep(2)
#
#     offcer.arrest(criminal)
#     time.sleep(2)
#
#     criminal.shoot(offcer)
#     time.sleep(2)
#
#     criminal.shoot(player1)
#     time.sleep(2)
#
#     player1.lay(criminal)
#     time.sleep(2)
#
#     player1.scary()
#     time.sleep(2)
#
#     player1.run()
#     time.sleep(2)
#
#     criminal.rob()
#     time.sleep(2)
#
#     worker.give(criminal)
#     time.sleep(2)
#
#     worker.layr(criminal)
#     time.sleep(2)
#
#     boss.work()
#     time.sleep(2)
#
#     boss.buy()
#     time.sleep(2)
#
#     boss.pay_taxes()
#     time.sleep(2)
#
#     boss.sell()
#     time.sleep(2)
#
#     print("\n --- Конец раунда ---")
#     time.sleep(3)


# import sqlite3
#
# class Book:
#     def __init__(self,title,author,year,genre,pages):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.genre = genre
#         self.pages = pages
#
#     def info(self):
#         print(f"Название: {self.title}")
#         print(f"Автор: {self.author}")
#         print(f"Год издание: {self.year}")
#         print(f"Жанр: {self.genre}")
#         print(f"Количество страниц: {self.pages}")
#         print(f"-" * 40)
#
# conn = sqlite3.connect('libary2.db')
# cursor = conn.cursor()
#
# #Создаем таблицу
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS books (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         author TEXT NOT NULL,
#         year INTEGER,
#         genre TEXT,
#         pages INTEGER
#     )
# ''')
# conn.commit()
#
# def add_book(title,author,year,genre,pages):
#     cursor.execute('''
#         INSERT INTO books(title,author,year,genre,pages)
#         VALUES (?,?,?,?,?)
#     ''',(title,author,year,genre,pages))
#     conn.commit()
#     print("Книга успешно добавлена!")
#
# def deleate_book(id):
#     cursor.execute('DELETE FROM books WHERE id = ?', (id,))
#     conn.commit()
#     print("Книга успешно добавлена в мусарку!")
#
# def display_all_books():
#     cursor.execute('''
#         SELECT * FROM books
#     ''')
#
#     books = cursor.fetchall()
#     if not books:
#         print("Библеотека пуста.")
#         return
#     for book in books:
#         print(f"ID: {book[0]}")
#         print(f"Название: {book[1]}")
#         print(f"Автор:{book[2]}")
#         print(f"Год издания:{book[3]}")
#         print(f"Жанр:{book[4]}")
#         print(f"Количество страниц:{book[5]}")
#         print(f"-" * 40)
#
# while True:
#     print("\n === Библиотечкая система ===")
#     print("1. Добавить книгу")
#     print("2. Прказать все книги")
#     print("3. удаление книги")
#     print("4. Выход")
#
#     choice = int(input("Выберите действие:"))
#     if choice == 1:
#         title = input("Введите название книге: ")
#         author = input("Введите автора книге: ")
#         year = input("Введите год издания книге: ")
#         genre = input("Введите жанр книге: ")
#         pages = input("Введите количество страниц:")
#         add_book(title,author,year,genre,pages)
#
#     if choice == 2:
#         display_all_books()
#
#     if choice == 3:
#         book_id = int(input("Введите id книги: "))
#         deleate_book(book_id)
#
#     if choice == 4:
#         break


# import sqlite3
# import time
#
#
# class Car:
#     def __init__(self,model,speed,color):
#         self.model = model
#         self.speed = speed
#         self.color = color
#
#     def info(self):
#         print(f"Модель машины: {self.model}")
#         print(f"Максимальноя скорость машины: {self.speed}")
#         print(f"Цвет машины: {self.color}")
#
# conn = sqlite3.connect('cars.db')
# cursor = conn.cursor()
#
# cursor.execute('''
#      CREATE TABLE IF NOT EXISTS cars (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#   	    model TEXT NOT NULL,
#   	    speed INTEGER,
#   	    color TEXT NOT NULL
#      )
#  ''')
# conn.commit()
#
#
# def add_car(model,speed,color):
#     cursor.execute('''
#              INSERT INTO cars(model,speed,color)
#              VALUES (?,?,?)
#     ''', (model,speed,color))
#     conn.commit()
#     print("Машина успешно добавлена!")
#
# def del_car(id):
#     cursor.execute('DELETE FROM cars WHERE id = ?', (id,))
#     conn.commit()
#
# def show_cars():
#     cursor.execute('''
#              SELECT * FROM cars
#     ''')
#
#     books = cursor.fetchall()
#     if not books:
#         print("Библеотека пуста.")
#         return
#     for book in books:
#         print(f"ID: {book[0]}")
#         print(f"Модель: {book[1]}")
#         print(f"Максимальноя скорость: {book[2]}")
#         print(f"Цвет: {book[3]}")
#         print(f"-" * 40)
#
# while True:
#     print(" === Библеотека Машин ===")
#     print("Добавить машину можно будет написав цифру: 1")
#     print("Удалить машину можно будет написав цифру: 2")
#     print("Посмотреть все машины можно будет написав цифру 3")
#     print("Выйти с системы вы моежете написав цифру 4")
#
#     choice = int(input("Выберите действия: "))
#     if choice == 1:
#         model = input("Модель: ")
#         speed = int(input("Максимальноя скорость: "))
#         color = input("Цвет: ")
#         add_car(model,speed,color)
#         time.sleep(3)
#
#     if choice == 2:
#         car_id = int(input("Введите id машины: "))
#         del_car(car_id)
#
#     if choice == 3:
#         show_cars()
#         time.sleep(3)
#
#     if choice == 4:
#         break


# from tkinter import *
# import random
#
# colors = ["black", "Blue", "Yellow","pink", "red", "orange", "brown"]
# window = Tk()
# window.title("My program")
#
#
# window.geometry("1080x1080")
# window.config(bg="white")
# score = 0
# def logic():
#     global score
#     score += 1
#     if score % 100 == 0:  # Меняем цвет только когда очки кратны 100
#         window.config(bg=random.choice(colors))
#     label1.config(text=score)
#
# def nol():
#     global score
#     score = 0
#     label1.config(text=score)
#
# def minus():
#     global score
#     if score > 0:
#         score -= 1
#         label1.config(text= score)
#     else:
#         score = 0
#         label1.config(text=score)
#
# label1 = Label(text = "Hi", font= "Arial 50", bg= "gold", fg= "purple")
# label1.place(x = 540,y = 540)
#
# label2 = Label(text= "my name is lior, *китайский* ni ne?", font= "comics 50", bg= "Blue", fg= "white")
# label2.place(x = 15, y = 440)
#
# butn = Button(text= "+", font= "Arial 30", bg= "black", fg= "white", width= 10, command= logic)
# butn.place(x = 460, y= 640)
#
# btn = Button(text= "-", font= "Arial 30",bg= "Black",fg= "White", width= 10,command= minus)
# btn.place(x = 460, y = 740)
#
# nol = Button(text= "сброс", font= "Arial 30",bg= "Black",fg= "White", width= 10,command= nol)
# nol.place(x = 460, y = 840)
#
#
#
#
# window.mainloop()

# import random
# from multiprocessing.connection import families
# from tkinter import *
# from tkinter.font import Font
#
# numbers = ["1","2","3","4","5","6","7","8","9","0" ]
# letters = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','!',
#     '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
#     ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
# ]
#
# password = ""
#
# window = Tk()
# window.title("🔐Генаратор паролей")
# window.resizable(False,False)
#
# def randomite():
#     global letters,numbers,password
#     password = ""
#     lenght = slider_length.get()
#     for i in range(lenght):
#         save = random.choice(numbers)
#         save_2 = random.choice(letters)
#         password += save
#         password += save_2
#         password_label.config(text= password)
#
#
#
# # window.geometry("500x450")
# # window.config(bg= "#f3f6fb")
# #
# # title_font = Font(family = "Segoe UI", size= 20, weight="bold")
# # label = Font(family= "Segoe UI", size= 12)
# # password_font = Font(family="Courier New", size= 18)
# #
# # title_label = Label(window, text = "Создай надежный пароль", font= title_font, bg="#f3f6fb", fg="#2c3e50")
# # title_label.pack(pady=20)
# #
# # password_label = Label(window, text="", font= password_font, width= 28, height=2,bg="White",fg="#2c3e50",bd=2, relief="flat",anchor="center")
# # password_label.pack(pady= 20)
# #
# # slider_frame = Frame(window, bg= "#f3f6fb")
# # slider_frame.pack(pady=10)
# #
# # length_label = Label(slider_frame, text= "Длина пароля: 12",font= label, bg="#f3f6fb", fg="#34495e")
# # length_label.pack()
# #
# # button_generate = Button(window, text="🔁 Создать пароль", font=("Segoe UI",14,"bold"), bg="#3499db", fg="White",padx=20,pady=10,relief="flat",bd=0, command=randomite,cursor="hand2",activebackground="#2980b9")
# # button_generate.pack(pady=15)
# #
# # slider_length = Scale(slider_frame, from_=6, to=30, orient=HORIZONTAL,
# #                       length=300, width=12, sliderlength=20, bd=0,
# #                       font=("Segoe UI", 10), bg="white", fg="#34495e",
# #                       highlightbackground="#f3f6fb", troughcolor="#dbe3ef")
# slider_length.set(12)
# slider_length.pack(pady=5)
# def upadate_length(val):
#     length_label.config(text=f"Длина пароля: {val}")
#
# slider_length.config(command=upadate_length)
#
#
# window.mainloop()

# import random
# from multiprocessing.connection import families
# from tkinter import *
# from tkinter.font import Font
#
#
# countries = [
#     "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
#     "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
#     "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
#     "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Congo (Congo-Kinshasa)",
#     "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic (Czechia)", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
#     "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Swaziland", "Ethiopia", "Fiji", "Finland", "France",
#     "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
#     "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan",
#     "Kenya", "Kiribati", "Korea (North)", "Korea (South)", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
#     "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
#     "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
#     "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
#     "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
#     "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan",
#     "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
#     "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu",
#     "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
#
# countries_generate = ""
#
# window = Tk()
# window.title("Страны")
# window.resizable(False,False)
#
# def randoamite():
#     global countries,countries_generate
#     for i in range(1):
#         show = random.choice(countries)
#         countries_ramdom.config(text=show)
#
#
# window.geometry("500x450")
# window.config(bg= "#f3f6fb")
#
#
# title_font = Font(family = "Segoe UI", size= 20, weight="bold")
# label = Font(family= "Segoe UI", size= 12)
# password_font = Font(family="Courier New", size= 18)
#
# title_label = Label(window, text = "Рандомноя страна", font= title_font, bg="#f3f6fb", fg="#2c3e50")
# title_label.pack(pady=20)
#
# countries_ramdom = Label(window, text="", font= password_font, width= 28, height=2,bg="White",fg="#2c3e50",bd=2, relief="flat",anchor="center")
# countries_ramdom.pack(pady= 20)
#
# button_generate = Button(window, text="Рандомноя страна", font=("Segoe UI",14,"bold"), bg="#3499db", fg="White",padx=20,pady=10,relief="flat",bd=0, command=randoamite,cursor="hand2",activebackground="#2980b9")
# button_generate.pack(pady=15)
#
#
# window.mainloop()

# from tkinter import *
# import random
#
# window = Tk()
# window.title("BlackJect 21")
# window.geometry("400x500")
# window.config(bg="#2c3e50")
#
# def set_bet(amount):
#     global current_bet
#     current_bet = amount
#     bet_label.config(text=f"Ставка: ${current_bet}")
#
#
# def new_game():
#     global deck, player_score,dealer_score
#     deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
#     random.shuffle(deck)
#     player_score = deck.pop() + deck.pop()
#     dealer_score = deck.pop() + deck.pop()
#     player_lable.config(text=f"Ваш счёт: {player_score}")
#     dealer_label.config(text=f"Счёт дилера: ?")
#     result_lable.config(text="")
#
# def stand():
#     global dealer_score, player_score, player_money
#     if current_bet == 0:
#         result_lable.config(text="Выбери ставку!", fg="orange")
#         return
#     while dealer_score < 17:
#         dealer_score += deck.pop()
#     dealer_label.config(text=f"Счёт дилера: {dealer_score}")
#     if dealer_score > 21 or player_score > dealer_score:
#         result_lable.config(text="Вы победили!", fg="green")
#         player_money += current_bet
#     elif player_score == dealer_score:
#         result_lable.config(text="Ничья!", fg="orange")
#     else:
#         result_lable.config(text="Вы проиграли!", fg="red")
#         player_money -= current_bet
#     player_money_label.config(text=f"${player_money}")
#
# def hit():
#     global player_score, player_money
#     if current_bet == 0:
#         result_lable.config(text="Выбери ставку!", fg="orange")
#         return
#     card = deck.pop()
#     player_score += card
#     player_lable.config(text=f"Ваш счёт: {player_score}")
#     if player_score > 21:
#         result_lable.config(text="Вы проиграли - перебор!", fg="red")
#         player_money -= current_bet
#         player_money_label.config(text=f"${player_money}")
#
# deck = [2,3,4,5,6,7,8,9,10,11] * 4
# random.shuffle(deck)
#
# player_score = 0
# dealer_score = 0
# player_money = 1000
# dealer_money = 10000000000000000
# current_bet = 0
#
# player_money_label = Label(window,text="$1000",font="Helvetica 20 bold", bg="#2c3e50",fg="green")
# player_money_label.pack(pady=10)
#
# player_lable = Label(window, text="", font= "Arial 16",bg="#2c3e50",fg="white")
# player_lable.pack(pady=10)
#
# bet_label = Label(window, text="Ставка: $0", font="Arial 14", bg="#2c3e50", fg="white")
# bet_label.pack(pady=5)
#
# dealer_label = Label(window,text= "Счёт дилера: ?", font="Arial 16",bg="#2c3e50", fg="lightgray")
# dealer_label.pack(pady=10)
#
# result_lable = Label(window,text="", font= "Arial 18 bold", fg="red",bg="#2c3e50")
# result_lable.pack(pady=10)
#
# btn_frame = Frame(window)
# btn_frame.pack(pady=10)
#
# hit_btn = Button(btn_frame, text= "Ещё", width=8, bg="#2c3e50",fg="white",command=hit)
# hit_btn.pack(side= LEFT, padx=5)
#
# stand_bth = Button(btn_frame,text="Хватит", width=8,bg="#2c3e50",fg="white",command=stand)
# stand_bth.pack(side= LEFT, padx=5)
#
# new_bth = Button(btn_frame,text="Новая",width=8, bg="#2c3e50",fg="white",command=new_game)
# new_bth.pack(side= LEFT,padx=5)
#
# title_label = Label(window,text="🃏 Блэкджек 21 🃏", font= "Helvetica 20 bold", bg="#2c3e50",fg="gold")
# title_label.pack(pady=15)
#
# five_btn = Button(window,text=500,font="Arial 16 bold",fg="#0d9000",bg="#bbb2a2",command=lambda:set_bet(500))
# five_btn.pack(pady=10)
#
# two_btn = Button(window,text=250,font="Arial 16 bold",fg="#0d9000",bg="#bbb2a2",command=lambda:set_bet(250))
# two_btn.place(x=100,y=376)
#
# thausend_btn = Button(window,text=1000,font="Arial 16 bold",fg="#0d9000",bg="#bbb2a2",command=lambda:set_bet(1000))
# thausend_btn.place(x=245,y=376)
#
#
# window.mainloop()