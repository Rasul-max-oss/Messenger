from optparse import Option
from typing import Dict, Optional, List

from fastapi import FastAPI, HTTPException
from flask import Response
from pydantic import BaseModel
from starlette import status

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#
#
# # Базовые статус-коды
# items_db = {}
#
#
# @app.post("/items/", status_code=201)
# def create_item(item: Item):
#     """Создание нового товара, возвращаем 201 Created"""
#     items_db[item.name] = item.price
#     return {"message": f"Item '{item.name}' created", "item": item}
#
#
# @app.get("/items/{item_name}")
# def get_item(item_name: str):
#     """Возвращаем разные статус-коды в зависимости от наличия товара"""
#     if item_name not in items_db:
#         # Возвращаем 404 если товар не найден
#         raise HTTPException(
#             status_code=404,  # ← status.HTTP_404_NOT_FOUND
#             detail=f"Item '{item_name}' not found"
#         )
#
#     # Возвращаем 200 OK если товар найден (по умолчанию)
#     return {"name": item_name, "price": items_db[item_name]}
#
#
# @app.delete("/items/{item_name}", status_code=204)
# def delete_item(item_name: str):
#     """Удаление товара, возвращаем 204 без тела ответа"""
#     if item_name in items_db:
#         del items_db[item_name]
#         # Для 204 статус-кода тело ответа не отправляется
#     # Если товара не было, все равно возвращаем 204




# users_db: Dict[int,dict] = {}
# next_id = 1
#
# #Пользователь отправляет
# class UserIN(BaseModel):
#     username: str
#     password: str
#     email: str
#
#
# #Что пользователь получает
# class UserOut(BaseModel):
#     id: int
#     username: str
#     email: str
#
#
# @app.post('/users',response_model=UserOut)
# def create_user(user: UserIN):
#     global next_id
#
#     users_db[next_id] = {
#         "username": user.username,
#         "password": user.password,
#         "email": user.email
#     }
#
#     reasponse_data = {
#         "id": next_id,
#         "username": user.username,
#         "email": user.email,
#         "password": user.password
#     }
#
#     next_id += 1
#     return reasponse_data
#
#
# # 5. ПОЛУЧЕНИЕ пользователя
# @app.get("/users/{user_id}", response_model=UserOut)
# def get_user(user_id: int):
#     """Получаем пользователя БЕЗ пароля"""
#     if user_id not in users_db:
#         raise HTTPException(status_code=404, detail="Пользователь не найден")
#
#     user = users_db[user_id].copy()
#     user["id"] = user_id
#
#     # В user есть пароль, но в ответе его не будет
#     return user
#
#
# # 6. ВСЕ пользователи
# @app.get("/users/", response_model=list[UserOut])
# def get_all_users():
#     """Список всех пользователей (без паролей)"""
#     result = []
#     for user_id, data in users_db.items():
#         result.append({
#             "id": user_id,
#             "username": data["username"],
#             "email": data["email"]
#         })
#     return result
#
#
# if __name__ == "__main__":
#     import uvicorn
#     print("🌐 http://127.0.0.1:8000")
#     print("📚 http://127.0.0.1:8000/docs")
#     uvicorn.run(app, host="127.0.0.1", port=8000)


