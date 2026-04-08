from datetime import datetime
from typing import Dict, Optional, List, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

class RubModel(BaseModel):
    rub: float

@app.post("/convert")
async def convert(rub_data: RubModel):
    usd = rub_data.rub / 90
    return {"usd": round(usd, 2)}










