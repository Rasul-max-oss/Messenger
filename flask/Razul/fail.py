# file = open("fail","r")
# content = file.read()
#
# print(content)
# file.close()
from calendar import month, weekday
from datetime import datetime

# with open("fail","r") as file:
#     content = file.read()
#     print(content)

# with open("data","w",encoding="utf-8") as fail:
#     fail.write("это первоя строка\n")
#     fail.write("Это вторая строка\n")

# with open("products","r") as file:
#     for line in file:
#         print(line.strip())

# shopping_list = ["Хлеб","Молоко","Яйца"]
# with open("products","a",encoding="utf-8") as file:
#     for item in shopping_list:
#         file.write(item + "\n")
#
# count = int(input("Введите количество товаров: "))
# for i in range(count):
#     item = input("Введите название предмета: ")
#     with open("products","a",encoding="utf-8") as file:
#         file.write(item + "\n")
#     print("Продукт успешно добавлен!")

# action = input("Введите действие: ")
# with open("log", "a",encoding="utf-8") as log_file:
#     from datetime import datetime
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     log_file.write(f"[{timestamp}] Пользователь сделал: {action}\n")

# from datetime import datetime
#
# now = datetime.now()
# print("Cейчас: ",now)
#
# today = datetime.today()
# print("Cегодня: ",today.date())
#
# start = datetime(2025,4,1)
# end = datetime(2025,4,10)
# delta = end - start
# print("Разница в днях:",delta.days)

# from datetime import datetime
#
# exam_date = datetime(2025,8,10)
# today = datetime.now()
# delta = exam_date - today
# print("До экзамена осталось ... ", delta)

# dt = datetime.now()
#
# year = dt.year
# month = dt.month
# day = dt.day
#
# hour = dt.hour
# minute = dt.minute
# second = dt.second
#
# weekday = dt.weekday() # 0-6
# isoweekday = dt.isoweekday() # 1-7
#
# date_only = dt.date()
# time_only = dt.time()
#
# print(year,month,day,hour,minute,second)
# print(weekday,isoweekday)
# print(date_only,time_only)

# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))
# print(now.strftime("%d/%m/%Y"))
# print(now.strftime("%H:%M:%S"))

# Y = int(input("Введите год рождение: "))
# M = int(input("Введите месяц рождение: "))
# D = int(input("Введите день рождение: "))
#
# now = datetime.now()
# birthday = datetime(Y,M,D)
# minus = now - birthday
# print("Вам:",minus.days//365,"лет/год(-а)")






















