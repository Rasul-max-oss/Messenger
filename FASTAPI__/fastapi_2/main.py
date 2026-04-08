from typing import List
import random
from fastapi import FastAPI


app = FastAPI(title="Случайные факты")

FACTS: List[str] = [
    "Мед никогда не портится. Археологи нашли мед возрастом 3000 лет, и он был съедобен.",
    "Осьминоги имеют три сердца.",
    "В Японии более 200 вулканов.",
    "Бананы - это ягоды, а клубника - нет.",
    "В Швейцарии запрещено иметь только одну морскую свинку, так как они скучают в одиночестве.",
    "Сердце голубого кита настолько большое, что через его артерии мог бы проплыть человек.",
    "Венера - единственная планета, которая вращается по часовой стрелке.",
    "Кошки могут издавать более 100 различных звуков, а собаки - только около 10.",
    "Человеческий нос может запомнить 50 000 различных ароматов.",
    "Снежинки состоят изо льда, но каждая имеет уникальную форму.",
    "Пингвины могут подпрыгивать на высоту до 2 метров.",
    "Морские выдры держатся за лапы во время сна, чтобы их не унесло течением.",
    "У улитки около 25 000 зубов.",
    "Свет от Солнца достигает Земли за 8 минут и 20 секунд.",
    "Крокодилы не могут высовывать язык."
]

FILMS: List[str] = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Forrest Gump",
    "Inception",
    "Fight Club",
    "The Matrix",
    "Interstellar",
    "Pulp Fiction",
    "Gladiator",
    "The Lord of the Rings",
    "Star Wars",
    "Back to the Future",
    "The Lion King",
    "Titanic",
    "Terminator 2",
    "The Green Mile",
    "Braveheart",
    "The Silence of the Lambs",
    "Pirates of the Caribbean"
]

QUOTES: List[str] = [
    "Hope is a good thing.",
    "I'm gonna make him an offer he can't refuse.",
    "Why so serious?",
    "Life is like a box of chocolates.",
    "You mustn't be afraid to dream a little bigger.",
    "The first rule of Fight Club…",
    "There is no spoon.",
    "Love is the one thing that transcends time and space.",
    "Say what again!",
    "Are you not entertained?",
    "One ring to rule them all.",
    "May the Force be with you.",
    "Great Scott!",
    "Remember who you are.",
    "I'm the king of the world!",
    "Hasta la vista, baby.",
    "I'm tired, boss.",
    "They may take our lives…",
    "Hello, Clarice.",
    "Why is the rum gone?"
]

# 1. Только символы (английские буквы)
symbols = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# 2. Только числа
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Всё вместе
all_items = symbols + numbers



@app.get('/')
def home():
    return {"Познание": "Добро пожаловать! тут вы узнаете много фактов и тут есть несколько режимов рандома!!"}

@app.get('/fact')
def fact():
    res = random.choice(FACTS)
    return {"Факт": f"{res}"}

@app.get('/film')
def film():
    res = random.choice(FILMS)
    return {"Фильм": f"{res}"}

@app.get('/quotes')
def quotes():
    res = random.choice(QUOTES)
    return {"Цитата": f"{res}"}


@app.post('/password')
def password(len: int, dig: bool, let: bool):
    global symbols, numbers, all_items
    res = ""
    if len < 4:
        return {"Ошибка": "Ваш пароль меньше 4 символов!"}

    # Проверяем оба случая отдельно
    for _ in range(len):
        if dig and let:
            res += random.choice(all_items)
        elif dig:  # только цифры
            res += random.choice(numbers)
        elif let:  # только буквы
            res += random.choice(symbols)
        else:
            # если оба False - используем все символы
            res += random.choice(all_items)

    return {"Результат": f"Ваш пароль {res}"}




