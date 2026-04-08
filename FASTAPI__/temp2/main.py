from lib2to3.fixes.fix_input import context

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import random



# Создаем приложение
app = FastAPI()

# Проверяем существование папки templates
templates_dir = "templates"
if not os.path.exists(templates_dir):
    os.makedirs(templates_dir)
    print(f"✅ Создана папка {templates_dir}")
else:
    print(f"✅ Папка {templates_dir} уже существует")

# Настраиваем шаблоны
templates = Jinja2Templates(directory=templates_dir)

world_facts = [
    "Земля не является идеальным шаром: она слегка сплюснута у полюсов.",
    "Марианская впадина глубже, чем высота Эвереста.",
    "Самый длинный горный хребет на планете находится под водой.",
    "Во время землетрясений вода в трещинах коры может превращаться в золото.",
    "Река Нил считается самой длинной в мире (6 853 км).",
    "Кофе — самый продаваемый продукт в мире после нефти.",
    "С ботанической точки зрения банан — это ягода, а клубника — нет.",
    "Стрижи могут проводить в воздухе несколько лет, не приземляясь.",
    "Кожа китов может обгорать на солнце, как и у людей.",
    "Попугаи Кеа в Новой Зеландии иногда нападают на овец.",
    "Растение Омежник вызывает ядовитую 'предсмертную улыбку'.",
    "Сердцебиение человека подстраивается под ритм музыки.",
    "Женское сердце в среднем бьется быстрее мужского.",
    "Существует гипотеза, что человек не видит сны во время храпа.",
    "Планета 55 Cancri e, по мнению ученых, состоит из алмазов."
]




@app.get('/',response_class=HTMLResponse)
async def get_fact(request: Request):
    ran = random.choice(world_facts)
    context = {"request": request,"ran": ran,"msg": "Все ок"}
    return templates.TemplateResponse(
        "index.html", context
    )

if __name__ == "__main__":
    print("🚀 Запуск сервера...")
    print("🌐 Откройте http://127.0.0.1:8000 в браузере")
    uvicorn.run(app, host="127.0.0.1", port=8000)



