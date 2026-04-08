from datetime import datetime
from typing import Dict
import random
from fastapi import FastAPI, HTTPException
from flask import Response
from jinja2.debug import rewrite_traceback_stack
from pydantic import BaseModel
from starlette import status

app = FastAPI()

reviews_db: Dict[int, dict] = {}
review_counter = 1

class ReviewCreate(BaseModel):
    product_id: int
    user_id: int
    rating: int
    comment: str
    user_email: str



class ReviewResponse(BaseModel):
    review_id: int
    product_id: int
    rating: int
    comment: str
    created_at: datetime


@app.post("/product",response_model=ReviewResponse)
def product_rating(r: ReviewCreate):
    global review_counter

    new_review = {
        "review_id": review_counter,
        "product_id": r.product_id,
        "user_id": r.user_id,
        "user_email": r.user_email,
        "rating": r.rating,
        "comment": r.comment,
        "created_at": datetime.utcnow()
    }

    reviews_db[review_counter] = new_review
    review_counter += 1

    return new_review







symbols = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# 2. Только числа
numbers = ['0','1','2','3','4','5','6','7','8','9']


# 3. Всё вместе
all_items = symbols + numbers


class UserResponse(BaseModel):
    password: str
    strength: str

@app.post('/password')
def create_password(lenght: int, num: bool = False,sym: bool = False):
    global symbols, numbers, all_items

    password = ""

    for _ in range(lenght):
        if num and sym:
            password += random.choice(all_items)
        elif num:
            password += random.choice(numbers)
        elif sym:
            password += random.choice(symbols)

    if lenght < 4:
        strength = "weak"
    elif lenght < 10:
        strength = "medium"
    else:
        strength = "hard"

    return {
        "Пароль": f"Ваш пароль {password}",
        "Безопасность": strength
    }










