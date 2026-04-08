# login = input("Введите логин: ")
#
# password = input("Введите пароль: ")
#
# if login == "1742" and password == "1742":
#    print("Вход свободен")
#
# else:
#    print("Вход запрешен")
import random
import time
from logging import fatal


# n = int(input("Введите число:"))
#
# if n > 0:
#    print("+")
# else:
#    print("-")


# city = input("Введите город:")
#
# age = int(input("Введите возрост:"))
#
# if city == "moscov" and age > 13:
#    print("Вход разрешон")
# else:
#    print("Вход запрешен ")

# mark = int(input("Введите число:"))
#
# if mark > 90:
#    print("отлично")
# elif mark > 75:
#    print("хорошо")
# elif mark > 60:
#    print("удов")
# else:
#    print("плохо")

# d = int(input("Введите число:"))
#
# if d == 1:
#    print("пн")
# elif d == 2:
#    print("вт")
# elif d == 3:
#    print("ср")
# elif d == 4:
#    print("чт")
# elif d == 5:
#    print("пт")
# elif d == 6:
#    print("сб")
# elif d == 7:
#    print("вс")
# else:
#    print("такого дня нету")


# b = int(input("Введите возрост:"))
#
# if b < 12:
#    print("Детские книги — для детей до 12 лет.")
# elif b > 12 and b < 17:
#    print("Юношеские книги — для подростков от 12 до 17 лет.")
# elif b > 17:
#    print("Взрослые книги — для людей старше 17 лет.")

# maseges = ["hi","lior","привет","я не спамер"]
# for i in range(100):
#     run = random.choice(maseges)
#     print(run)
#     time.sleep(0.1)

# for i in range(5):
#     user = input("введите канфету:")
#     if user == "festable":
#         print("ты смотреш Mr.beast")
#     else:
#         print("ты не круотй")

# m = int(input("Введите число:"))
# n = int(input("Введите число:"))
#
# for i in range(m,n):
#     print(i)

# for _ in range(10):
#     print("Python is awesome!")

# t = int(input("Введите число:"))
# m = input("Введите слово:")
#
# for _ in range(t):
#     print(m)

# for _ in range(6):
#     print("aaaa")
# for _ in range(5):
#     print("bbbb")
# print("e")
# for _ in range(8):
#     print("tttt")
# print("g")

# n = input("write your name:")
#
# for i in range(10):
#     print(i,n)

# for i in range(2,6):
#     print(i,"Это мое любимое число:")

# a = int(input("Введите ряд звездочек:"))
#
# star = "********"
#
# for _ in range(a):
#     print(star)
#
# a = int(input("Введите число:"))
#
# for i in range(a):
#     print("квадрат число", i ,"равно", i * i)

# import random
#
# life = 5
# secret = random.randint(1,100)
# print("Добро пожаловать в игру:")
# print("Ваи нужно угадать число от 1-100")
# print(" у вас в наличие:", life,"жизней" )
# round = 1
# print("вы можете выбрать уровень сложности:")
# print("500 - легко - 1:20")
# print("501 - средний - 1:50")
# print("502 - тежолый - 1:100")
# print("503- гайд")
#
#
# while True:
#     print("----раунд:", round, "----")
#
#     user = int(input("Введите число:"))
#     if user == 1000:
#         password = input("Введите пароль:")
#         if password == "admin":
#             print(secret)
#     if user == 500:
#         secret = random.randint(1,20)
#         print("Уровень игры изменен на легко")
#         continue
#     if user == 501:
#         secret = random.randint(1, 50)
#         print("Уровень игры изменен на средний")
#         continue
#     if user == 502:
#         secret = random.randint(1, 100)
#         print("Уровень игры изменен на тежолый")
#         continue
#     if user == 503:
#         print("ВЫ попали на гайд по игре:"
#               "Для того чтобы начять игру вам надо выбрать уровень сложности,"
#               "дальше в все зовисет от уровня:"
#               "легкий уровень он от 1-20, сам компютор выберает вам число и вам надо его отгодать."
#               "так же средний уровень он от 1-50,"
#               "и тежолый от 1-100.")
#         continue
#     life -= 1
#     round += 1
#     print("Жизни:", life)
#     if life <= 0:
#         print("Проиграл")
#         choice = input("Хотите продолжеть ?")
#         if choice == "да":
#             if user == 500:
#                 secret = random.randint(1, 20)
#                 print("Уровень игры изменен на легко")
#                 continue
#             if user == 501:
#                 secret = random.randint(1, 50)
#                 print("Уровень игры изменен на средний")
#                 continue
#             if user == 502:
#                 secret = random.randint(1, 100)
#                 print("Уровень игры изменен на тежолый")
#                 continue
#             secret = random.randint(1,100)
#             life = 5
#             round = 1
#             print("игра перезапускается")
#             continue
#         else:
#             print("пока")
#             break
#     if user == secret:
#         print("Угадал!!")
#         choice = input("Хотите продолжеть ?")
#         if choice == "да" or choice == "yes":
#             if user == 500:
#                 secret = random.randint(1, 20)
#                 print("Уровень игры изменен на легко")
#                 continue
#             if user == 501:
#                 secret = random.randint(1, 50)
#                 print("Уровень игры изменен на средний")
#                 continue
#             if user == 502:
#                 secret = random.randint(1, 100)
#                 print("Уровень игры изменен на тежолый")
#                 continue
#             # secret = random.randint(1, 100)
#             life = 5
#             round = 1
#             print("игра перезапускается")
#             continue
#         else:
#             print("пока")
#             break
#     elif user > secret:
#         print("Число менше")
#     else:
#         print("Число Больше")

# sta = ["gta", "roblox", "war", "cola"]
# print(sta)
# print(sta[0])
# print(sta[2])
# print(sta[-1])

# speed = [100, 230, 400, 123]
# print(speed[2] + speed[3])

# films = ["spiderman", "doctor strange", "Venom", "Squid game"]
#
# if "spiderman" in films:
#     print("yes")
# else:
#     print("No")

# curt = []
#
# count = int(input("Введите количество товаров: "))
#
# for i in range(count):
#     user = input("Введите название товара: ")
#     curt.append(user)
#     print("Товар добавлен")
# print("Ваши товары:",curt)

# game = ["камень", "ножницы", "бумага"]
# print("Добро пожалуйста в игру 'Камень, Ножницы, Бумага'!")
# print("Введите 'выход' для завершения игры.")
# state_user = 0
# stat_computer = 0
# money = 0
#
# while True:
#     user_choice = input("Введите ваш выбор (камень, ножницы, бумага):")
#     if user_choice == "выход":
#         print("пока")
#         break
#     computer_choice = random.choice(game)
#     print(f"Компьютор выбрал: {computer_choice}")
#     if user_choice == computer_choice:
#         print("Ничья")
#     elif(user_choice == "камень" and computer_choice == "ножницы") or (user_choice == "ножницы" and computer_choice == "бумага") or (user_choice == "бумага" and computer_choice == "камень"):
#         state_user += 1
#         money += 100
#         print("Win:",state_user)
#     else:
#         stat_computer += 1
#         money -=100
#         print("Компютор выйграл:", stat_computer)

# game = ["gta","roblox","minecraft"]
#
# print(game[1])
# game.append("war")
# game.append("mtrp")
#
# for i in game:
#     print(i)
#
# user = input("Введите игру:")
#
# if user in game:
#     print("Yes")
# else:
#     print("No")

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71]
#
# print(primes[-1])

# lan = ["hebrew", "russain", "english"]
#
# if "english" in lan:
#     print("good")
# else:
#     print("bad")
#
# print(lan[0],lan[-1])
#
# lan.append("frace")
# lan.append("kazax")
#
# for i in lan:
#     print(i)

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
#  53, 59, 61, 67, 71]
#
# print(primes[0]+primes[-1])

# computer = {
#     "Rtx": "4060ti",
#     "Age": 2,
#     "ram": "32gb",
#     "Ssd": "2tr"
# }
#
# for key,value in computer.items():
#     print(key,"-",value,)

# object = [
#     {
#         "Name": "gta",
#         "rating": "10/10",
#     },
#     {
#         "Name": "Cyber-bank",
#         "rating": "9/10"
#     },
#     {
#         "Name": "Roblox",
#         "rating": "8/10"
#     }
# ]
#
# for i in object:
#     print(i["Name"],"-",i["rating"])

# books = {
#     "1": "Война и мир, Лев Толстой, 1869",
#     "2": "Преступление и наказание, Федор Достоевский, 1866",
#     "3": "Мастер и Маргарита, Михаил Булгаков, 1967",
#     "4": "1984, Джордж Оруэлл, 1949",
#     "5": "Гарри Поттер и философский камень, Дж. К. Роулинг, 1997"
# }
#
# user = input("Введите номер книги:")
#
# if user in books:
#     print("Информация о книге:",books[user])

# def hello():
#     print("Привет !")
#
# hello()
#
# def Weather():
#     print("Сенодня хорошая погода")
#
# Weather()
#
# def welcome_user(name):
#     print("привет!", name)
#
# welcome_user("Лиор")
#
# def summa(a,b):
#     print(a + b)
#
# summa(1,10)
#
# def summa_2(a,b,c):
#     print(a * b * c)
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# summa_2(a,b,c)

# def face_control(age):
#     if age > 18:
#         print("Yes Enter!")
#     else:
#         print("NO Enter!!")
#
# age = int(input("Age:"))
#
# face_control(age)

# def number(n):
#     if n %2 == 0:
#         print("Четное")
#     else:
#         print("Не четное")
#
# number(float(input()))

# def number(n):
#     if n > 0:
#         print("Положительное")
#     else:
#         print("Отрецательное")
#
# number(float(input()))

# def film():
#     import random
#     films = ["Venom","Barbi","Lucifer","Spiderman","Last of us"]
#     random_film = random.choice(films)
#     print(random_film)
#
# def game():
#     game = ["камень", "ножницы", "бумага"]
#     print("Добро пожалуйста в игру 'Камень, Ножницы, Бумага'!")
#     print("Введите 'выход' для завершения игры.")
#     state_user = 0
#     stat_computer = 0
#     money = 0
#
#     while True:
#         user_choice = input("Введите ваш выбор (камень, ножницы, бумага):")
#         if user_choice == "выход":
#             print("пока")
#             break
#         computer_choice = random.choice(game)
#         print(f"Компьютор выбрал: {computer_choice}")
#         if user_choice == computer_choice:
#             print("Ничья")
#         elif(user_choice == "камень" and computer_choice == "ножницы") or (user_choice == "ножницы" and computer_choice == "бумага") or (user_choice == "бумага" and computer_choice == "камень"):
#             state_user += 1
#             money += 100
#             print("Win:",state_user)
#         else:
#             stat_computer += 1
#             money -=100
#             print("Компютор выйграл:", stat_computer)
#
# def help():
#     print("/help - показовает команды.")
#     print("/fact - Показовает факт.")
#     print("/citata - Показовает случайную цитату.")
#     print("/film - Показовает случайный фильм.")
#     print("/game - У вас есть дрступ к игре.")
#     print("/pictur - раскажет вам о кокойто картине.")
#     print("/language - выберет вам язык для учебы.")
#     print("/name - даст вам имя.")
#     print("/animal - даст вам имя.")
#     print("/drink - даст вам пите на вечер.")
#     print("/item - выдаст вам вещь на котором вы будете смотреть фильм или играть.")
#     print("/program - даст вам програму в которай вы будете смотреть чтото.")
#
# def pictur():
#     picturs = ["mona-lisa", "picaso","micelangelo"]
#     random_pictur = random.choice(picturs)
#     print(random_pictur)
#
# def language():
#     languages = ["hebrew","russain","english","Germany","Spanish","Italiano","Franch"]
#     random_language = random.choice(languages)
#     print(random_language)
#
# def name():
#     names = ["lior","rasul","shasa","peta","kate"]
#     random_name = random.choice(names)
#     print(random_name)
#
# def animal():
#     animals = ["cat","dog","cow","fish","duck"]
#     random_animal = random.choice(animals)
#     print(random_animal)
#
# def drink():
#     drinks = ["vine","bear","cola/pepsi","water","juice"]
#     random_drink = random.choice(drinks)
#     print(random_drink)
#
# def item():
#     items = ["computer","phone","TV","tablet"]
#     random_item = random.choice(items)
#     print(random_item)
#
# def program():
#     programs = ["tiktok","instagram","YouTube","FaceBook"]
#     random_program = random.choice(programs)
#     print(random_program)
#
# while True:
#     user= input("Введите команду:")
#      if user == "/help":
#          help()
#      if user == "/film":
#          film()
#      if user == "/game":
#          game()
#      if user == "/pictur":
#          pictur()
#      if user == "/language":
#          language()
#      if user == "/name":
#          name()
#      if user == "/animal":
#          animal()
#      if user == "/drink":
#          drink()
#      if user == "/item":
#         item()
#     if user == "/program":
#         program()

# import random
# import time
# import sys
#
#
# WORDS = [
#     "программирование", "алгоритм", "переменная",
#     "функция", "цикл", "условие", "список",
#     "словарь", "класс", "объект", "модуль",
#     "библиотека", "разработка", "интерфейс"
# ]
#
# print("__________________")
# print("Игра: Быстрый набор слов")
# print("___________________")
# print("Правила:")
# print("1.Вводите слова, которое появится на экране")
# print("2. У вас есть 5 секунд на каждое слово")
# print("3. За правтльное ответ +1 очко")
# print("4. Для выхода введите 'выход'")
# print("_______________________________")
# input("Нажмити ENTER чтобы начать...")
#
# score = 0
# start_time = time.time()
# while True:
#     word = random.choice(WORDS)
#     print(f"Наберите:{word}")
#     end_time = time.time() + 10
#     while time.time() < end_time:
#         user = input()
#         if user == "Exit" or user == "выход":
#             print(f" игра окончена. Ваш счет {score}")
#             break
#         if user == word:
#             score += 1
#             print(f"Верно! Ваш счет {score}")
#             break
#         else:
#             print(f"Неверно! ожидалось:{word}")
#             score -= 1
#             print(f"Ваш счет.{score}")
#             break
#     else:
#         print(f"nВремя вышло! слово было:{word} ")

# import random
#
# def info():
#     print("words - просто слова - 1")
#     print("knifes - ножы - 2")
#     print("game - вещи связаные с играми - 3")
#     print("nature - природа - 4")
#     print("magic - вещи связаные с магией - 5")
#     print("months - месеца - 6")
#
# words = ["питон", "программа", "компьютер", "клавиатура", "монитор", "мышка","экран","автобус","адрес","боль","труд","учеба","память","низкий","парень"]
#
# knifes = ["ложка","вилка","нож","пила","кинжал","кирамбит"]
#
# game = ["игрок","игра","мир","команды","админы","помошники","помащь"]
#
# nature = ["природа","парк","растение","цветы","лес","дерева","вода"]
#
# magic = ["заклинание","зелие","кровь","голова","приношения","книжка"]
#
# months = ["Январь","февряль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
#
# secret_word = random.choice(words)
# attempts = 10
# guessed_letters = []
#
# def menu():
#     global secret_word
#     global attempts
#     global guessed_letters
#
#     print("Добро пожаловать в игру Угадай слово")
#     print(f"у вас есть {attempts} попыток")
#     print("Слово состоит из",len(secret_word))
#     print("Введите команду (/info) чтобы узнать какие есть вирианты")
#
#     user = input("Введите команду:")
#
#
#
#     if user == "admin":
#         print("Вам доступна 2 команды")
#         print("1. выбор темы")
#         print("2. убрать попутки")
#         user_choice = int(input("Введите число:"))
#         if user_choice == 1:
#             info()
#             user_choice = int(input("Введите число:"))
#             if user_choice == 1:
#                 secret_word = random.choice(words)
#             elif user_choice == 2:
#                 secret_word = random.choice(knifes)
#             elif user_choice == 3:
#                 secret_word = random.choice(game)
#             elif user_choice == 4:
#                 secret_word = random.choice(nature)
#             elif user_choice == 5:
#                 secret_word = random.choice(magic)
#             elif user_choice == 6:
#                 secret_word = random.choice(months)
#             else:
#                 print("Такой команды нет")
#             print(f"Вот слова:{secret_word},только тихо!!")
#         elif user_choice == 2:
#             attempts = 999
#     if user == "/info":
#         info()
#         user_choice = int(input("Введите число:"))
#         if user_choice == 1:
#             secret_word = random.choice(words)
#         elif user_choice == 2:
#             secret_word = random.choice(knifes)
#         elif user_choice == 3:
#             secret_word = random.choice(game)
#         elif user_choice == 4:
#             secret_word = random.choice(nature)
#         elif user_choice == 5:
#             secret_word = random.choice(magic)
#         elif user_choice == 6:
#             secret_word = random.choice(months)
#         else:
#             print("Такой команды нет")
#
# menu()
#
# while attempts > 0:
#     display_word = ""
#     for latter in secret_word:
#         if latter in guessed_letters:
#             display_word += latter
#         else:
#             display_word += "_"
#     print("Слово:",display_word)
#     if "_" not in display_word:
#         print("Вы угадали")
#         user_choice = input("Хотите продолжить:")
#         if user_choice == "да":
#             secret_word = random.choice(words)
#             attempts = 10
#             guessed_letters = []
#             menu()
#             continue
#         else:
#             print("Поки")
#             break
#     user = input("Введите букву:")
#     if len(user)!= 1 or not user.isalpha():
#         print("Пожалуйста введите одну букву, но не число")
#         continue
#     if user in guessed_letters:
#         print("Вы уже назвали эту букву")
#         continue
#     guessed_letters.append(user)
#     if user not in secret_word:
#         attempts -= 1
#         print(f"Такой буквы нет! осталось попыток:{attempts}")
# else:
#     print(f"К сожелению, вы проиграли. Загадоное слово было:{secret_word}")

# a = 10
# b = 20
# c = 30
# d = 40
# print(a+b+c+d)

# user = int(input("Напишите свой возрасть:"))
#
# if user >= 18:
#     print("Вход свободен")
# else:
#     print("Вход запрещен")

# name = "Lior"
#
# for i in range(20):
#     print(name)

# for i in range(20):
#     if i %2 == 0:
#         print(i)

# game = ["cs2","dota2","roblox","gta5","matrehska"]
# game.append("minecraft")
#
# print(game)

# user = int(input("введите количество товара:"))
#
# tovar = []
#
# for i in range(user):
#     user_choice = input("Введите названия товара:")
#     tovar.append(user_choice)
# print(f"Ваш товар:",tovar)

# base = {
#     "student 1": "петя, 2 курс, живет с друзьями",
#     "student 2": "федр, 3 курс, проживает в квартире",
#     "student 3": "настя, 1 курс, проживает с родителями"
# }
#
# user_age = int(input("Введите ваш возраст:"))
#
# def age(user_age):
#     if user_age >= 18:
#         print("Вы наш студент")
#     else:
#         print("Вы не наш студент!")
# age(user_age)

# user_1 = int(input("Число:"))
# user_2 = int(input("Число:"))
#
# def number(user_1,user_2):
#     print(user_1 + user_2)
# number(user_1,user_2)

import time

money = 100

cart = []


def info_product_buy():
    print("1. Яблоко = 100")
    print("2. Груша = 200")
    print("3. Ягоды = 150")
    print("4. Торт = 300")
    print("5. Котики = 1000")
    print("6. Сигареты = 300")
    print("7. Кортошка = 200")
    print("8. Велосипед = 10000")
    print("9. Вода = 50")
    print("10. Пива = 600")
    print("11. Вино = 1500")
    print("12. Квас = 450")

def info_product_sell():
    print("1. Яблоко = 120")
    print("2. Груша = 240")
    print("3. Ягоды = 180")
    print("4. Торт = 360")
    print("5. Котики = 1200")
    print("6. Сигареты = 450")
    print("7. Кортошка = 240")
    print("8. Велосипед = 12000")
    print("9. Вода = 60")
    print("10. Пива = 720")
    print("11. Вино = 1800")
    print("12. Квас = 530")

def info_item():
    print("Команда 1-я (Купить): /buy")
    print("Команда 2-я (Продать): /sell")

def next():
    user = input("Хотите ли вы продолжить покупку?")
    if user == "Yes" or user == "Да":
        return True
    else:
        return False

while True:
    info_item()
    user_choice = input("Введити команду:")
    if user_choice == "admin":
        money = 100000
        while True:
            info_product_buy()
            user_product = int(input("Выберите номер товара:"))
            if user_product == 1:
                if money >= 10:
                    money -= 10
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Яюлоко")
                else:
                    print("У вас недостаточно средств")
            if user_product == 2:
                if money >= 20:
                    money -= 20
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Груша")
                else:
                    print("У вас недостаточно средств")
            if user_product == 3:
                if money >= 15:
                    money -= 15
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Ягоды")
                else:
                    print("У вас недостаточно средств")
            if user_product == 4:
                if money >= 30:
                    money -= 30
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Торт")
                else:
                    print("У вас недостаточно средств")
            if user_product == 5:
                if money >= 100:
                    money -= 100
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Котики")
                else:
                    print("У вас недостаточно средств")
            if user_product == 6:
                if money >= 30:
                    money -= 30
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Сигареты")
                else:
                    print("У вас недостаточно средств")
            if user_product == 7:
                if money >= 20:
                    money -= 30
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Кортошка")
                else:
                    print("У вас недостаточно средств")
            if user_product == 8:
                if money >= 1000:
                    money -= 1000
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Велосипед")
                else:
                    print("У вас недостаточно средств")
            if user_product == 9:
                if money >= 5:
                    money -= 5
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Вода")
                else:
                    print("У вас недостаточно средств")
            if user_product == 10:
                if money >= 60:
                    money -= 60
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Пиво")
                else:
                    print("У вас недостаточно средств")
            if user_product == 11:
                if money >= 150:
                    money -= 150
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Вино")
                else:
                    print("У вас недостаточно средств")
            if user_product == 12:
                if money >= 45:
                    money -= 45
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Вино")
                else:
                    print("У вас недостаточно средств")
            user_next = next()
            if user_next:
                continue
            else:
                break
            if user_choice == "/sell":
                print(f"Ваша товары{cart}")
                time.sleep(5)
                info_product_sell()
                user_sell = int(input("Введите номер того товара который вы хотите продать:"))
                if user_sell == 1:
                    if "Яблоко" in cart:
                        money += 150 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Яблоко")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 2:
                    if "Груша" in cart:
                        money += 300 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Груша")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 3:
                    if "Ягоды" in cart:
                        money += 215 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Ягоды")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 4:
                    if "Торт" in cart:
                        money += 450 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Торт")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 5:
                    if "Котики" in cart:
                        money += 1500 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Котики")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 6:
                    if "Сигареты" in cart:
                        money += 450 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Сигареты")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 7:
                    if "Кортошка" in cart:
                        money += 300 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Кортошка")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 8:
                    if "Велосипед" in cart:
                        money += 10000 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Велосипед")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 9:
                    if "Вода" in cart:
                        money += 50 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Вода")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 10:
                    if "Пива" in cart:
                        money += 600 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Пива")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 11:
                    if "Вино" in cart:
                        money += 1500 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Вино")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
                if user_sell == 12:
                    if "Квас" in cart:
                        money += 450 * 10
                        print("Успешноя продажа")
                        print(f"Ваш баланс:{money}")
                        cart.remove("Квас")
                    else:
                        print("Вы не покупали данный товар!(обманшик)")
    if user_choice == "/buy":
        while True:
            info_product_buy()
            user_product = int(input("Выберите номер товара:"))
            if user_product == 1:
                if money >= 100:
                    money -= 100
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Яблоко")
                else:
                    print("У вас недостаточно средств")
            if user_product == 2:
                if money >= 200:
                    money -= 200
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Груша")
                else:
                    print("У вас недостаточно средств")
            if user_product == 3:
                if money >= 150:
                    money -= 150
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Ягоды")
                else:
                    print("У вас недостаточно средств")
            if user_product == 4:
                if money >= 300:
                    money -= 300
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Торт")
                else:
                    print("У вас недостаточно средств")
            if user_product == 5:
                if money >= 1000:
                    money -= 1000
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Котики")
                else:
                    print("У вас недостаточно средств")
            if user_product == 6:
                if money >= 300:
                    money -= 300
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Сигареты")
                else:
                    print("У вас недостаточно средств")
            if user_product == 7:
                if money >= 200:
                    money -= 300
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Кортошка")
                else:
                    print("У вас недостаточно средств")
            if user_product == 8:
                if money >= 10000:
                    money -= 10000
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Велосипед")
                else:
                    print("У вас недостаточно средств")
            if user_product == 9:
                if money >= 50:
                    money -= 50
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Вода")
                else:
                    print("У вас недостаточно средств")
            if user_product == 10:
                if money >= 600:
                    money -= 600
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Пиво")
                else:
                    print("У вас недостаточно средств")
            if user_product == 11:
                if money >= 1500:
                    money -= 1500
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Вино")
                else:
                    print("У вас недостаточно средств")
            if user_product == 12:
                if money >= 450:
                    money -= 450
                    print(f"Ваш текущий баланс:{money}")
                    cart.append("Котики")
                else:
                    print("У вас недостаточно средств")
            user_next = next()
            if user_next:
                continue
            else:
                break
    if user_choice == "/sell":
        print(f"Ваша товары{cart}")
        time.sleep(5)
        info_product_sell()
        user_sell = int(input("Введите номер того товара который вы хотите продать:"))
        if user_sell == 1:
            if "Яблоко" in cart:
                money += 150 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Яблоко")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 2:
            if "Груша" in cart:
                money += 300 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Груша")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 3:
            if "Ягоды" in cart:
                money += 215 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Ягоды")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 4:
            if "Торт" in cart:
                money += 450 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Торт")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 5:
            if "Котики" in cart:
                money += 1500 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Котики")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 6:
            if "Сигареты" in cart:
                money += 450 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Сигареты")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 7:
            if "Кортошка" in cart:
                money += 300 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Кортошка")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 8:
            if "Велосипед" in cart:
                money += 10000 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Велосипед")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 9:
            if "Вода" in cart:
                money += 50 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Вода")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 10:
            if "Пива" in cart:
                money += 600 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Пива")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 11:
            if "Вино" in cart:
                money += 1500 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Вино")
            else:
                print("Вы не покупали данный товар!(обманшик)")
        if user_sell == 12:
            if "Квас" in cart:
                money += 450 * 0.2
                print("Успешноя продажа")
                print(f"Ваш баланс:{money}")
                cart.remove("Квас")
            else:
                print("Вы не покупали данный товар!(обманшик)")


