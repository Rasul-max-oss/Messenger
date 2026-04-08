from typing import Dict, Optional, List, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import session
from fastapi.middleware.cors import CORSMiddleware
import random


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

@app.get('/')
async def root():
    return {"Msg": "Hello from server"}


@app.get('/home')
async def home():
    return {
        "First": "Lior",
        "Last": "Poli.",
        "City": "Haifa",
        "Age": 14
    }


@app.get('/random')
async def get_number():
    res = random.randint(0,100)
    return {"Number": res}









