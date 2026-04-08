from enum import Enum
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from models import Player, SessionLocal, engine


Player.metadata.create_all(bind=engine)
app = FastAPI()



class Skill(BaseModel):
    level: int = Field(default=1,ge=1,le=100)

class ItemType(str,Enum):
    FOOD = "food"
    MEDICINE = "medicine"
    TOOL = "tool"
    OTHER = "other"

class Item(BaseModel):
    name: str
    item_type: ItemType
    value: int = Field(default=1,ge=1)
    quantity: int = Field(default=1,ge=0)
    price: int = Field(default=0,ge=0)
    description: str = ""



class PlayerState(BaseModel):
    health: int = Field(default=100,ge=0,le=100,description="Здоровья")
    food: int = Field(default=100,ge=0,le=100,description="Голод")
    energy: int = Field(default=100,ge=0,le=100,description="Энергия")
    money: int = Field(default=0,ge=0,le=10000,description="Деньги")
    day: int = Field(default=0,ge=0,le=1000,description="Дни")
    exp: int = Field(default=1,ge=1,le=100000,description="Здоровья")
    happiness: int = Field(default=100,ge=0,le=100,description="настроение")
    skills: Dict[str,Skill] = Field(default_factory=lambda: {"Power": Skill(level=1),"Intellect": Skill(level=1),"Agility": Skill(level=1)})
    inventory: Dict[str,Item] = Field(default_factory=dict,description="Инвентарь персонажа")

    def add_item(self, item:Item):
        if item.name in self.inventory:
            self.inventory[item.name].quantity += item.quantity
        else:
            self.inventory[item.name] = item




player = PlayerState()

@app.post('/add_player')
def add_player():
    db = SessionLocal()

    new_player = Player()
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    db.close()

    return {"Msg": "Игрок создан", "id": new_player.id}




@app.get('/work')
def work(hours: int):
    db = SessionLocal()
    player = db.query(Player).first()

    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Игрок не найден")

    if player.energy <= 10:
        raise HTTPException(
            status_code=450,
            detail="Персонаж устал!"
        )
    if player.food <= 5:
        raise HTTPException(
            status_code=451,
            detail="Персонаж голоден!"
        )

    zp = player.exp * player.day + 150
    player.money += zp
    player.energy -= 10

    db.commit()
    db.refresh(player)
    db.close()

    return {"Статус": f"Успешно добавилось {player.money} денег!"}

@app.get("/stats")
def show_stats():
    db = SessionLocal()
    player = db.query(Player).first()
    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Игрок не найден")
    db.close()
    return player


@app.get('/skills')
def get_skills(hours: int,power: bool = False, intellect: bool = False,agility: bool = False ):
    db = SessionLocal()
    player = db.query(Player).first()

    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Игрок не найден")

    if player.energy <= 10:
        raise HTTPException(
            status_code=450,
            detail="Персонаж устал!"
        )

    skills = player.skills

    if player.food <= 5:
        raise HTTPException(
            status_code=451,
            detail="Персонаж голоден!"
        )

    if hours <= 2:
        raise HTTPException(
            status_code=461,
            detail="Мало часов отработал"
        )

    if 2 < hours <= 5:
        bonus = 1
    elif 5 < hours <= 8:
        bonus = 2
    else:
        bonus = 5

    if power:
        skills["Power"]["level"] += bonus
        return {"Прокачено": f"+{bonus}"}
    elif intellect:
        skills["Intellect"]["level"] += bonus
        return {"Прокачено": f"+{bonus}"}
    elif agility:
        skills["Agility"]["level"] += bonus
        return {"Прокачено": f"+{bonus}"}

    player.skills = skills
    player.energy -= 10


    db.commit()
    db.refresh(player)
    db.close()


@app.post('/add_item')
def add_item_to_inventory(item: Item):
    db = SessionLocal()
    player = db.query(Player).first()

    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Игрок не найден")

    if not item.name or not item.item_type or not item.description:
        raise HTTPException(
            status_code=521,
            detail="Вы не добавили имя или тип или описание предмета!"
        )

    inventory = player.inventory

    if item.name in inventory:
        inventory[item.name]["quantity"] += item.quantity
    else:
        inventory[item.name] = item.dict()

    player.inventory=inventory

    db.commit()
    db.refresh(player)
    db.close()

    return {
        "Статус": "Успешно",
        "Инвентарь": player.inventory
    }





if __name__ == "__main__":
    import uvicorn
    print("🌐 http://127.0.0.1:8000")
    print("📚 http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)