import uvicorn
import datetime
import json
from fastapi import FastAPI, Depends, Form, HTTPException, Request, Response, WebSocket
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, or_, and_, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import UniqueConstraint

# 1. База данных
DB_URL = "sqlite:///./users.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def encrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

key = "Messenger_Max"

class GroupChat(Base):
    __tablename__ = "group_chats"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    avatar = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    number = Column(Integer, unique=True)
    password = Column(String)
    adders = Column(String)
    avatar = Column(String)
    description = Column(String,nullable=True)


class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    user1_id = Column(Integer, ForeignKey("users.id"))
    user2_id = Column(Integer, ForeignKey("users.id"))


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String)
    timestamp = Column(String)
    is_delivered = Column(Boolean, default=True)  # Доставлено (отправлено на сервер)
    is_read = Column(Boolean, default=False)  # Прочитано собеседником
    is_deleted_globally = Column(Boolean, default=False)  # Удалено у всех
    is_deleted_for_sender = Column(Boolean, default=False)  # Удалено у отправителя
    is_deleted_for_receiver = Column(Boolean, default=False)  # Удалено у получателя

class Block(Base):
    __tablename__ = "blocks"
    id = Column(Integer, primary_key=True, index=True)
    blocker_id = Column(Integer, ForeignKey("users.id"))
    blocked_id = Column(Integer, ForeignKey("users.id"))


class GroupMember(Base):
    __tablename__ = "group_members"
    id = Column(Integer, primary_key=True, index=True)
    group_chat_id = Column(Integer, ForeignKey("group_chats.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    joined_at = Column(String)
    __table_args__ = (UniqueConstraint('group_chat_id', 'user_id', name='_group_user_uc'),)


class GroupMessage(Base):
    __tablename__ = "group_messages"
    id = Column(Integer, primary_key=True, index=True)
    group_chat_id = Column(Integer, ForeignKey("group_chats.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String)
    timestamp = Column(String)
    is_deleted = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# ===== МЕНЕДЖЕР WEBSOCKET ПОДКЛЮЧЕНИЙ =====
class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, list[WebSocket]] = {}

    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = []
        self.active_connections[user_id].append(websocket)

    def disconnect(self, user_id: int, websocket: WebSocket):
        if user_id in self.active_connections:
            self.active_connections[user_id].remove(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]

    async def send_notification(self, user_id: int, data: dict):
        """Отправить уведомление пользователю"""
        if user_id in self.active_connections:
            for websocket in self.active_connections[user_id]:
                try:
                    await websocket.send_json(data)
                except Exception:
                    pass


manager = ConnectionManager()


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(user_id, websocket)
    db = SessionLocal()
    try:
        while True:
            data = await websocket.receive_json()
            
            # Обработка разных типов сообщений
            if data.get("type") == "typing":
                # Можно добавить обработку статуса "печатает"
                pass
            elif data.get("type") == "mark_as_delivered":
                # Отмечаем сообщение как доставленное
                message_id = data.get("message_id")
                if message_id:
                    msg = db.query(Message).filter(Message.id == message_id).first()
                    if msg:
                        msg.is_delivered = True
                        db.commit()
                        
                        # Уведомляем отправителя
                        await manager.send_notification(msg.sender_id, {
                            "type": "message_delivered",
                            "message_id": message_id,
                            "chat_id": msg.chat_id
                        })
    except Exception:
        manager.disconnect(user_id, websocket)
    finally:
        db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(request: Request, db: Session = Depends(get_db)):
    """Получить текущего пользователя по cookie"""
    user_id = request.cookies.get("user_id")
    if not user_id:
        return None
    return db.query(User).filter(User.id == int(user_id)).first()


# --- МАРШРУТЫ ---

@app.get('/')
def register_page(request: Request):
    return templates.TemplateResponse("register.html", context={"request": request})


@app.get('/login_page')
def login_page(request: Request):
    return templates.TemplateResponse('login.html', context={"request": request})


@app.post('/register')
def register(
        username: str = Form(...),
        number: int = Form(...),
        adders: str = Form(...),
        avatar: str = Form(...),
        password: str = Form(...),
        db: Session = Depends(get_db)
):
    existing = db.query(User).filter(User.number == number).first()
    if existing:
        return {"error": "Пользователь с таким номером уже существует"}

    Pass = encrypt(password, key)
    add = encrypt(adders, key)

    new_user = User(username=username, number=number, adders=add, avatar=avatar, password=Pass)
    db.add(new_user)
    db.commit()
    return RedirectResponse(url="/login_page", status_code=303)


@app.post('/login')
def login(username: str = Form(...), number: int = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    check = db.query(User).filter(User.username == username, User.password == encrypt(password, key), User.number == number).first()
    if not check:
        return RedirectResponse('/login_page', status_code=303)

    response = RedirectResponse('/profile', status_code=303)
    response.set_cookie(key="user_id", value=str(check.id))
    return response


@app.get('/profile')
def profile_page(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse("/login_page", status_code=303)

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        return RedirectResponse("/login_page", status_code=303)

    return templates.TemplateResponse("profile.html", context={"request": request, "user": user})


@app.get('/logout')
def logout():
    response = RedirectResponse(url="/login_page", status_code=303)
    response.delete_cookie("user_id")
    return response


@app.get('/chats')
def chats_page(request: Request, db: Session = Depends(get_db)):
    # Получаем user_id из cookies
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse("/login_page", status_code=303)


    return templates.TemplateResponse("messenger.html", context={"request": request})


# ===== API ЭНДПОИНТЫ =====
@app.get('/api/chats')
def api_get_chats(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    chats = db.query(Chat).filter(
        or_(Chat.user1_id == current_user_id, Chat.user2_id == current_user_id)
    ).all()

    result = []
    for chat in chats:
        partner_id = chat.user2_id if chat.user1_id == current_user_id else chat.user1_id
        partner = db.query(User).filter(User.id == partner_id).first()
        
        # Проверяем, не заблокировал ли партнёр меня
        blocked_by_partner = db.query(Block).filter(
            Block.blocker_id == partner_id,
            Block.blocked_id == current_user_id
        ).first()
        
        # Проверяем, не заблокировал ли я партнёра
        blocked_by_me = db.query(Block).filter(
            Block.blocker_id == current_user_id,
            Block.blocked_id == partner_id
        ).first()
        
        # Последнее сообщение (не удаленное)
        last_msg = db.query(Message).filter(
            Message.chat_id == chat.id,
            Message.is_deleted_globally == False
        ).order_by(Message.id.desc()).first()
        
        # Расшифровываем текст последнего сообщения, если оно есть
        last_message_text = None
        if last_msg:
            last_message_text = encrypt(last_msg.text, key)  # РАСШИФРОВЫВАЕМ
        
        result.append({
            "chat_id": chat.id,
            "partner": {
                "id": partner.id,
                "username": partner.username,
                "number": partner.number,
                "adders": encrypt(partner.adders, key),  # Расшифровываем адрес
                "avatar": partner.avatar,
                "description": partner.description,
                "is_blocked_by_me": blocked_by_me is not None,
                "is_blocked_by_partner": blocked_by_partner is not None
            },
            "last_message": {
                "text": last_message_text,
                "timestamp": last_msg.timestamp if last_msg else None
            } if last_msg else None
        })

    return result


@app.get('/api/messages/{chat_id}')
def api_get_messages(chat_id: int, request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        return {"error": "Чат не найден"}

    if chat.user1_id != current_user_id and chat.user2_id != current_user_id:
        return {"error": "Нет доступа"}

    messages = db.query(Message).filter(Message.chat_id == chat_id).order_by(Message.id).all()

    result = []
    for msg in messages:
        # Пропускаем полностью удаленные сообщения
        if msg.is_deleted_globally:
            continue
        
        # Пропускаем сообщения, удаленные для текущего пользователя
        if msg.sender_id == current_user_id and msg.is_deleted_for_sender:
            continue
        if msg.sender_id != current_user_id and msg.is_deleted_for_receiver:
            continue
        
        result.append({
            "id": msg.id,
            "text": encrypt(msg.text, key),  # РАСШИФРОВЫВАЕМ для отображения
            "timestamp": msg.timestamp,
            "is_mine": msg.sender_id == current_user_id,
            "is_delivered": msg.is_delivered,
            "is_read": msg.is_read
        })
    
    return result

@app.post('/api/send_message/{chat_id}')
async def api_send_message(
    chat_id: int,
    request: Request,
    text: str = Form(...),
    db: Session = Depends(get_db)
):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    # Находим чат и определяем собеседника
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        return {"error": "Чат не найден"}

    partner_id = chat.user2_id if chat.user1_id == current_user_id else chat.user1_id

    # Проверяем, не заблокирован ли текущий пользователь собеседником
    block_check = db.query(Block).filter(
        Block.blocker_id == partner_id,
        Block.blocked_id == current_user_id
    ).first()
    
    if block_check:
        return {"error": "Вы заблокированы этим пользователем"}

    # Проверяем, не заблокировал ли текущий пользователь собеседника
    block_check_reverse = db.query(Block).filter(
        Block.blocker_id == current_user_id,
        Block.blocked_id == partner_id
    ).first()
    
    if block_check_reverse:
        return {"error": "Вы заблокировали этого пользователя. Разблокируйте его, чтобы отправлять сообщения."}

    new_message = Message(
        chat_id=chat_id,
        sender_id=current_user_id,
        text=encrypt(text, key),
        timestamp=str(datetime.datetime.now().strftime("%H:%M")),
        is_delivered=True,  # Сообщение доставлено на сервер
        is_read=False  # Ещё не прочитано
    )

    db.add(new_message)
    db.commit()

    # Уведомляем собеседника о новом сообщении через WebSocket
    await manager.send_notification(partner_id, {
        "type": "new_message",
        "chat_id": chat_id,
        "message": {
            "id": new_message.id,
            "text": text,
            "timestamp": new_message.timestamp,
            "sender_id": current_user_id
        }
    })

    # Отправляем отправителю подтверждение с актуальными статусами
    # Проверяем, онлайн ли собеседник
    is_partner_online = partner_id in manager.active_connections
    
    return {
        "status": "ok",
        "message_id": new_message.id,
        "is_delivered": True,
        "is_read": False,
        "partner_online": is_partner_online
    }


@app.post('/api/add_number')
def api_add_number(request: Request, number: int = Form(...), db: Session = Depends(get_db)):
    current_user_id = request.cookies.get("user_id")
    if not current_user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(current_user_id)
    target_user = db.query(User).filter(User.number == number).first()

    if not target_user or target_user.id == current_user_id:
        return {"error": "Пользователь не найден"}

    existing_chat = db.query(Chat).filter(
        or_(
            and_(Chat.user1_id == current_user_id, Chat.user2_id == target_user.id),
            and_(Chat.user1_id == target_user.id, Chat.user2_id == current_user_id)
        )
    ).first()

    blocked_user = db.query(Block).filter(Block.blocked_id == target_user.id, Block.blocker_id == current_user_id).first()
    if blocked_user:
         raise HTTPException(status_code=510, detail="Вы заблокировали этого пользователя. Разблокируйте его, чтобы начать чат.")

    if existing_chat:
        return {
            "chat_id": existing_chat.id,
            "partner": {
                "id": target_user.id,
                "username": target_user.username,
                "number": target_user.number,
                "adders": encrypt(target_user.adders, key),
                "avatar": target_user.avatar,
                "description": target_user.description
            }
        }

    new_chat = Chat(user1_id=current_user_id, user2_id=target_user.id)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)

    return {
        "chat_id": new_chat.id,
        "partner": {
            "id": target_user.id,
            "username": target_user.username,
            "number": target_user.number,
            "adders": encrypt(target_user.adders, key),
            "avatar": target_user.avatar,
            "description": target_user.description
        }
    }


# ===== ЭНДПОИНТЫ ДЛЯ СТАТУСОВ СООБЩЕНИЙ =====

@app.post('/api/mark_as_read/{chat_id}')
async def api_mark_as_read(chat_id: int, request: Request, db: Session = Depends(get_db)):
    """Отметить все сообщения в чате как прочитанные"""
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        return {"error": "Чат не найден"}

    if chat.user1_id != current_user_id and chat.user2_id != current_user_id:
        return {"error": "Нет доступа"}

    # Определяем отправителя сообщений (собеседника)
    sender_id = chat.user2_id if chat.user1_id == current_user_id else chat.user1_id

    # Находим все непрочитанные сообщения от собеседника
    unread_messages = db.query(Message).filter(
        Message.chat_id == chat_id,
        Message.sender_id == sender_id,
        Message.is_read == False
    ).all()

    updated_count = 0
    updated_message_ids = []
    for msg in unread_messages:
        msg.is_read = True
        msg.is_delivered = True
        updated_message_ids.append(msg.id)
        updated_count += 1

    db.commit()

    # Уведомляем собеседника, что его сообщения прочитаны
    if updated_count > 0:
        await manager.send_notification(sender_id, {
            "type": "messages_read",
            "chat_id": chat_id,
            "reader_id": current_user_id,
            "message_ids": updated_message_ids
        })

    return {
        "status": "ok",
        "updated_count": updated_count,
        "message_ids": updated_message_ids
    }


@app.get('/api/message_status/{chat_id}')
def api_get_message_status(chat_id: int, request: Request, db: Session = Depends(get_db)):
    """Получить статусы сообщений в чате (для синхронизации при открытии)"""
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        return {"error": "Чат не найден"}

    if chat.user1_id != current_user_id and chat.user2_id != current_user_id:
        return {"error": "Нет доступа"}

    # Получаем все сообщения, где sender == current_user (мои сообщения)
    my_messages = db.query(Message).filter(
        Message.chat_id == chat_id,
        Message.sender_id == current_user_id
    ).all()

    return {
        "messages": [
            {
                "id": msg.id,
                "is_delivered": msg.is_delivered,
                "is_read": msg.is_read
            }
            for msg in my_messages
        ]
    }


@app.get('/add_number_page')
def add_number_page(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse("/login_page", status_code=303)

    user = db.query(User).filter(User.id == int(user_id)).first()
    return templates.TemplateResponse("add_number.html", context={"request": request, "user": user})


@app.get('/settings_page')
def settings_page(request: Request,db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse("/login_page", status_code=303)

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        return RedirectResponse("/login_page", status_code=303)

    return templates.TemplateResponse('/settings.html', context={"request": request, "user": user})

@app.post('/settings')
def settings(request: Request,name: str = Form(None),password: str = Form(None),avatar: str = Form(None),description:str = Form(None),db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    user = db.query(User).filter(User.id == int(user_id)).first()

    if user:
        if name:
            user.username = name
        if password:
            user.password = encrypt(password, key)  
        if avatar:
            user.avatar = avatar
        if description:
            user.description = description
        db.commit()


    return RedirectResponse('/profile',status_code=303)


@app.delete('/api/delete_message/{message_id}')
async def api_delete_message(message_id: int, request: Request, db: Session = Depends(get_db)):
    """Удалить сообщение у всех (полное удаление)"""
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    message = db.query(Message).filter(Message.id == int(message_id)).first()
    if not message:
        return {"error": "Сообщение не найдено"}

    # Только отправитель может удалить сообщение у всех
    if message.sender_id != current_user_id:
        return {"error": "Нет доступа"}

    message.is_deleted_globally = True
    db.commit()

    # Уведомляем собеседника о удалении
    receiver_id = None
    chat = db.query(Chat).filter(Chat.id == message.chat_id).first()
    if chat:
        receiver_id = chat.user2_id if chat.user1_id == current_user_id else chat.user1_id
        await manager.send_notification(receiver_id, {
            "type": "message_deleted",
            "message_id": message_id,
            "chat_id": message.chat_id
        })

    return {"status": "ok", "message": "Сообщение удалено у всех", "partner_id": receiver_id}


@app.delete('/api/delete_message_self/{message_id}')
async def api_delete_message_self(message_id: int, request: Request, db: Session = Depends(get_db)):
    """Удалить сообщение только у себя"""
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    message = db.query(Message).filter(Message.id == int(message_id)).first()
    if not message:
        return {"error": "Сообщение не найдено"}

    # Проверяем доступ
    chat = db.query(Chat).filter(Chat.id == message.chat_id).first()
    if not chat or (chat.user1_id != current_user_id and chat.user2_id != current_user_id):
        return {"error": "Нет доступа"}

    # Помечаем удаление в зависимости от того, отправитель это или получатель
    if message.sender_id == current_user_id:
        message.is_deleted_for_sender = True
    else:
        message.is_deleted_for_receiver = True

    db.commit()

    return {"status": "ok", "message": "Сообщение удалено у вас"}


@app.delete('/api/delete_chat/{chat_id}')
def api_delete_chat(chat_id: int, request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        return {"error": "Чат не найден"}

    if chat.user1_id != current_user_id and chat.user2_id != current_user_id:
        return {"error": "Нет доступа"}

    # Удаляем все сообщения в чате
    db.query(Message).filter(Message.chat_id == chat_id).delete()
    # Удаляем сам чат
    db.delete(chat)
    db.commit()

    return {"status": "ok", "message": "Чат удалён"}   


@app.put('/api/edit_message/{message_id}')
async def api_edit_message(message_id: int, request: Request, new_text: str = Form(...), db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    message = db.query(Message).filter(Message.id == int(message_id)).first()
    if not message:
        return {"error": "Сообщение не найдено"}

    # Только отправитель может редактировать сообщение
    if message.sender_id != current_user_id:
        return {"error": "Нет доступа"}

    message.text = encrypt(new_text, key)  # Сохраняем отредактированный текст в зашифрованном виде
    db.commit()

    # Уведомляем собеседника о редактировании
    receiver_id = None
    chat = db.query(Chat).filter(Chat.id == message.chat_id).first()
    if chat:
        receiver_id = chat.user2_id if chat.user1_id == current_user_id else chat.user1_id
        await manager.send_notification(receiver_id, {
            "type": "message_edited",
            "message_id": message_id,
            "chat_id": message.chat_id,
            "new_text": new_text,
            "timestamp": message.timestamp
        })

    return {"status": "ok", "message": "Сообщение отредактировано", "new_text": new_text, "new_timestamp": message.timestamp}

@app.get('/show_information/{user_id}')
def show_information(request: Request, user_id: int, db: Session = Depends(get_db)):
    current_user_id = request.cookies.get("user_id")
    if not current_user_id:
        return RedirectResponse("/login_page", status_code=303)

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "Пользователь не найден"}



    return templates.TemplateResponse("show_information.html", context={"request": request, "user": user})

@app.post('/block_user/{user_id}')
def block_user(request: Request, user_id: int, db: Session = Depends(get_db)):
    current_user = request.cookies.get("user_id")
    if not current_user:
        return {"error": "Не авторизован"}
    
    current_user_id = int(current_user)
    target_user = db.query(User).filter(User.id == user_id).first()
    if not target_user:
        return {"error": "Пользователь не найден"}  
    
    if user_id == current_user_id:   
        return {"error": "Нельзя заблокировать самого себя"}
    
    # Проверяем, не заблокирован ли уже этот пользователь
    existing_block = db.query(Block).filter(
        Block.blocker_id == current_user_id,
        Block.blocked_id == user_id
    ).first()
    
    if existing_block:
        return {"error": "Пользователь уже заблокирован"}
    
    # Создаём блокировку
    new_block = Block(blocker_id=current_user_id, blocked_id=user_id)
    db.add(new_block)
    db.commit()

    # Удаляем чат с заблокированным пользователем
    current_chat = db.query(Chat).filter(
        or_(
            and_(Chat.user1_id == current_user_id, Chat.user2_id == user_id),
            and_(Chat.user1_id == user_id, Chat.user2_id == current_user_id)
        )
    ).first()
    
    if current_chat:
        db.query(Message).filter(Message.chat_id == current_chat.id).delete()
        db.commit()

    return {"status": "ok", "message": "Пользователь заблокирован"}


@app.post('/api/block_user/{user_id}')
async def api_block_user(user_id: int, request: Request, db: Session = Depends(get_db)):
    """API для блокировки пользователя из чата"""
    current_user = request.cookies.get("user_id")
    if not current_user:
        return JSONResponse({"error": "Не авторизован"}, status_code=401)
    
    current_user_id = int(current_user)
    target_user = db.query(User).filter(User.id == user_id).first()
    if not target_user:
        return JSONResponse({"error": "Пользователь не найден"}, status_code=404)
    
    if user_id == current_user_id:   
        return JSONResponse({"error": "Нельзя заблокировать самого себя"}, status_code=400)
    
    # Проверяем, не заблокирован ли уже этот пользователь
    existing_block = db.query(Block).filter(
        Block.blocker_id == current_user_id,
        Block.blocked_id == user_id
    ).first()
    
    if existing_block:
        return JSONResponse({"error": "Пользователь уже заблокирован"}, status_code=400)
    
    # Создаём блокировку
    new_block = Block(blocker_id=current_user_id, blocked_id=user_id)
    db.add(new_block)
    db.commit()

    # НЕ удаляем чат - оставляем его для возможности разблокировки
    # Chat остаётся нетронутым

    return {"status": "ok", "message": "Пользователь заблокирован"}


@app.delete('/api/unblock_user/{user_id}')
def api_unblock_user(user_id: int, request: Request, db: Session = Depends(get_db)):
    """API для разблокировки пользователя"""
    current_user = request.cookies.get("user_id")
    if not current_user:
        return JSONResponse({"error": "Не авторизован"}, status_code=401)
    
    current_user_id = int(current_user)
    
    # Ищем блокировку
    block_record = db.query(Block).filter(
        Block.blocker_id == current_user_id,
        Block.blocked_id == user_id
    ).first()
    
    if not block_record:
        return JSONResponse({"error": "Пользователь не заблокирован"}, status_code=404)
    
    # Удаляем блокировку
    db.delete(block_record)
    db.commit()

    return {"status": "ok", "message": "Пользователь разблокирован"}

@app.get('/group_chat_page')
def group_chat_page(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse("/login_page", status_code=303)

    return templates.TemplateResponse("group_chat.html", context={"request": request})


@app.get('/api/emojis')
def api_emojis():
    return [
        "😀", "😁", "😂", "🤣", "😊", "😍", "😘", "😎",
        "🤔", "😢", "😭", "😡", "👍", "🙏", "🔥", "❤️"
    ]


@app.post('/api/create_group_chat')
def api_create_group_chat(request: Request, name: str = Form(...), description: str = Form(...), avatar: str = Form(...), db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)

    new_group_chat = GroupChat(
        name=name,
        description=description,
        avatar=avatar,
        creator_id=current_user_id
    )
    db.add(new_group_chat)
    db.commit()
    db.refresh(new_group_chat)
    
    # Добавляем создателя в группу
    creator_member = GroupMember(
        group_chat_id=new_group_chat.id,
        user_id=current_user_id,
        joined_at=str(datetime.datetime.now().strftime("%H:%M"))
    )
    db.add(creator_member)
    db.commit()

    return {
        "status": "ok",
        "group_chat_id": new_group_chat.id,
        "message": "Групповой чат создан"
    }


@app.post('/api/add_user_to_group/{group_chat_id}')
async def api_add_user_to_group(group_chat_id: int, request: Request, number: int = Form(...), db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    
    # Проверяем, существует ли группа
    group = db.query(GroupChat).filter(GroupChat.id == group_chat_id).first()
    if not group:
        return {"error": "Группа не найдена"}
    
    # Проверяем, является ли текущий пользователь создателем или членом группы
    member = db.query(GroupMember).filter(
        GroupMember.group_chat_id == group_chat_id,
        GroupMember.user_id == current_user_id
    ).first()
    
    if not member:
        return {"error": "Вы не в этой группе"}
    
    # Находим пользователя по номеру
    target_user = db.query(User).filter(User.number == number).first()
    if not target_user:
        return {"error": "Пользователь с таким номером не найден"}
    
    if target_user.id == current_user_id:
        return {"error": "Вы уже в этой группе"}
    
    # Проверяем, не в группе ли уже пользователь
    existing_member = db.query(GroupMember).filter(
        GroupMember.group_chat_id == group_chat_id,
        GroupMember.user_id == target_user.id
    ).first()
    
    if existing_member:
        return {"error": "Этот пользователь уже в группе"}
    
    # Добавляем пользователя в группу
    new_member = GroupMember(
        group_chat_id=group_chat_id,
        user_id=target_user.id,
        joined_at=str(datetime.datetime.now().strftime("%H:%M"))
    )
    db.add(new_member)
    db.commit()
    
    # Уведомляем нового члена группы
    await manager.send_notification(target_user.id, {
        "type": "added_to_group",
        "group_chat_id": group_chat_id,
        "group_name": group.name
    })
    
    return {
        "status": "ok",
        "message": "Пользователь добавлен в группу",
        "user": {
            "id": target_user.id,
            "username": target_user.username,
            "number": target_user.number,
            "avatar": target_user.avatar
        }
    }


@app.get('/api/group_chats')
def api_get_group_chats(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    
    # Получаем все группы, в которых участвует пользователь
    members = db.query(GroupMember).filter(GroupMember.user_id == current_user_id).all()
    
    result = []
    for member in members:
        group = db.query(GroupChat).filter(GroupChat.id == member.group_chat_id).first()
        
        # Последнее сообщение в группе
        last_msg = db.query(GroupMessage).filter(
            GroupMessage.group_chat_id == group.id,
            GroupMessage.is_deleted == False
        ).order_by(GroupMessage.id.desc()).first()
        
        last_message_text = None
        if last_msg:
            last_message_text = encrypt(last_msg.text, key)
        
        # Получаем количество членов группы
        members_count = db.query(GroupMember).filter(GroupMember.group_chat_id == group.id).count()
        
        result.append({
            "group_chat_id": group.id,
            "name": group.name,
            "description": group.description,
            "avatar": group.avatar,
            "creator_id": group.creator_id,
            "members_count": members_count,
            "last_message": {
                "text": last_message_text,
                "timestamp": last_msg.timestamp if last_msg else None
            } if last_msg else None
        })
    
    return result


@app.get('/api/group_members/{group_chat_id}')
def api_get_group_members(group_chat_id: int, request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    
    # Проверяем, в группе ли текущий пользователь
    member = db.query(GroupMember).filter(
        GroupMember.group_chat_id == group_chat_id,
        GroupMember.user_id == current_user_id
    ).first()
    
    if not member:
        return {"error": "Вы не в этой группе"}
    
    # Получаем группу
    group = db.query(GroupChat).filter(GroupChat.id == group_chat_id).first()
    if not group:
        return {"error": "Группа не найдена"}
    
    # Получаем членов группы
    members = db.query(GroupMember).filter(GroupMember.group_chat_id == group_chat_id).all()
    
    result = []
    for member in members:
        user = db.query(User).filter(User.id == member.user_id).first()
        result.append({
            "user_id": user.id,
            "username": user.username,
            "number": user.number,
            "avatar": user.avatar,
            "is_creator": user.id == group.creator_id
        })
    
    return {
        "group": {
            "id": group.id,
            "name": group.name,
            "description": group.description,
            "avatar": group.avatar,
            "creator_id": group.creator_id
        },
        "members": result
    }


@app.get('/api/group_messages/{group_chat_id}')
def api_get_group_messages(group_chat_id: int, request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    
    # Проверяем, в группе ли текущий пользователь
    member = db.query(GroupMember).filter(
        GroupMember.group_chat_id == group_chat_id,
        GroupMember.user_id == current_user_id
    ).first()
    
    if not member:
        return {"error": "Вы не в этой группе"}
    
    # Получаем сообщения сразу вместе с данными отправителей (оптимизация)
    messages_with_users = db.query(GroupMessage, User).outerjoin(
        User, GroupMessage.sender_id == User.id
    ).filter(
        GroupMessage.group_chat_id == group_chat_id,
        GroupMessage.is_deleted == False
    ).order_by(GroupMessage.id).all()
    
    result = []
    for msg, sender in messages_with_users:
        result.append({
            "id": msg.id,
            "text": encrypt(msg.text, key),
            "timestamp": msg.timestamp,
            "sender_id": msg.sender_id,
            "sender_username": sender.username if sender else "Unknown",
            "sender_avatar": sender.avatar if sender else "",
            "is_mine": msg.sender_id == current_user_id
        })
    
    return result


@app.post('/api/send_group_message/{group_chat_id}')
async def api_send_group_message(
    group_chat_id: int,
    request: Request,
    text: str = Form(...),
    db: Session = Depends(get_db)
):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    
    # Проверяем существование группы и членство пользователя
    group = db.query(GroupChat).filter(GroupChat.id == group_chat_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Группа не найдена")

    member = db.query(GroupMember).filter(
        GroupMember.group_chat_id == group_chat_id,
        GroupMember.user_id == current_user_id
    ).first()
    
    if not member:
        raise HTTPException(status_code=403, detail="Вы не являетесь участником этой группы")
    
    # Получаем информацию об отправителе заранее
    sender = db.query(User).filter(User.id == current_user_id).first()
    if not sender:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # --- Дополнительная проверка: не заблокирован ли отправитель в группе? ---
    # В текущей схеме нет механизма блокировки внутри группы,
    # но если бы он был, проверка шла бы здесь.
    # Например, если бы GroupMember имел поле `is_muted` или `is_blocked_by_creator`.
    # Поскольку такой логики нет, это не является причиной текущего бага.
    # Но это место для потенциальных будущих проверок.

    # Создаём сообщение
    new_message = GroupMessage(
        group_chat_id=group_chat_id,
        sender_id=current_user_id,
        text=encrypt(text, key),
        timestamp=str(datetime.datetime.now().strftime("%H:%M")),
        is_deleted=False
    )
    
    db.add(new_message)
    db.commit() # Commit to get the message ID
    db.refresh(new_message) # Refresh to ensure new_message.id is populated
    
    # Собираем данные для уведомления
    notification_data = {
        "type": "new_group_message",
        "group_chat_id": group_chat_id,
        "message": {
            "id": new_message.id,
            "text": text,
            "timestamp": new_message.timestamp,
            "sender_id": current_user_id,
            "sender_username": sender.username,
            "sender_avatar": sender.avatar
        }
    }

    # Рассылаем уведомления в фоне, не дожидаясь завершения для каждого пользователя
    import asyncio
    members = db.query(GroupMember.user_id).filter(GroupMember.group_chat_id == group_chat_id).all()
    for (m_id,) in members:
        asyncio.create_task(manager.send_notification(m_id, {**notification_data, "message": {**notification_data["message"], "is_mine": m_id == current_user_id}}))
    
    return {
        "status": "ok",
        "message_id": new_message.id,
        "timestamp": new_message.timestamp, # Include timestamp in response for immediate display on sender's side
        "is_delivered": True # Indicate that it was delivered to the server
    }


@app.delete('/api/delete_group_message/{message_id}')
async def api_delete_group_message(message_id: int, request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    
    message = db.query(GroupMessage).filter(GroupMessage.id == message_id).first()
    if not message:
        return {"error": "Сообщение не найдено"}
    
    # Только отправитель может удалить сообщение
    if message.sender_id != current_user_id:
        return {"error": "Нет доступа"}
    
    message.is_deleted = True
    db.commit()
    
    # Уведомляем всех членов группы об удалении
    members = db.query(GroupMember).filter(GroupMember.group_chat_id == message.group_chat_id).all()
    for member in members:
        await manager.send_notification(member.user_id, {
            "type": "group_message_deleted",
            "message_id": message_id,
            "group_chat_id": message.group_chat_id
        })
    
    return {"status": "ok", "message": "Сообщение удалено"}

@app.put('/api/edit_group_message/{message_id}')
async def api_edit_group_message(message_id: int, request: Request, new_text: str = Form(...), db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    
    message = db.query(GroupMessage).filter(GroupMessage.id == message_id).first()
    if not message:
        return {"error": "Сообщение не найдено"}
    
    # Только отправитель может редактировать
    if message.sender_id != current_user_id:
        return {"error": "Нет доступа"}
    
    message.text = encrypt(new_text, key)
    db.commit() # Commit to save changes
    db.refresh(message) # Refresh to ensure message.timestamp is current (though it doesn't change in this schema)
    
    # Уведомляем всех членов группы через WebSocket
    members = db.query(GroupMember).filter(GroupMember.group_chat_id == message.group_chat_id).all()
    for member in members:
        await manager.send_notification(member.user_id, {
            "type": "group_message_edited",
            "message_id": message_id,
            "group_chat_id": message.group_chat_id,
            "new_text": new_text, # Отправляем расшифрованный текст для отображения
            "timestamp": message.timestamp
        })
    
    return {
        "status": "ok",
        "new_text": new_text
    }

@app.delete('/api/remove_user_from_group/{group_chat_id}/{remove_user_id}')
async def api_remove_user_from_group(group_chat_id: int, remove_user_id: int, request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    
    # Получаем группу
    group = db.query(GroupChat).filter(GroupChat.id == group_chat_id).first()
    if not group:
        return {"error": "Группа не найдена"}
    
    # Проверяем, является ли текущий пользователь создателем
    if group.creator_id != current_user_id and current_user_id != remove_user_id:
        return {"error": "Нет прав"}
    
    # Удаляем пользователя из группы
    member = db.query(GroupMember).filter(
        GroupMember.group_chat_id == group_chat_id,
        GroupMember.user_id == remove_user_id
    ).first()
    
    if not member:
        return {"error": "Пользователь не в группе"}
    
    db.delete(member)
    db.commit()
    
    # Уведомляем удаляемого пользователя
    await manager.send_notification(remove_user_id, {
        "type": "removed_from_group",
        "group_chat_id": group_chat_id
    })
    
    return {"status": "ok", "message": "Пользователь удалён из группы"}


@app.delete('/api/delete_group_chat/{group_chat_id}')
async def api_delete_group_chat(group_chat_id: int, request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    
    # Получаем группу
    group = db.query(GroupChat).filter(GroupChat.id == group_chat_id).first()
    if not group:
        return {"error": "Группа не найдена"}
    
    # Проверяем, является ли текущий пользователь создателем
    if group.creator_id != current_user_id:
        return {"error": "Только создатель может удалить группу"}
    
    # Удаляем всех членов группы
    db.query(GroupMember).filter(GroupMember.group_chat_id == group_chat_id).delete()
    
    # Удаляем все сообщения группы
    db.query(GroupMessage).filter(GroupMessage.group_chat_id == group_chat_id).delete()
    
    # Удаляем саму группу
    db.delete(group)
    db.commit()
    
    return {"status": "ok", "message": "Группа удалена"}

@app.put('/api/update_group_settings/{group_chat_id}')
async def api_update_group_settings(
    group_chat_id: int, 
    request: Request, 
    name: str = Form(None), 
    description: str = Form(None), 
    db: Session = Depends(get_db)
):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return {"error": "Не авторизован"}

    current_user_id = int(user_id)
    group = db.query(GroupChat).filter(GroupChat.id == group_chat_id).first()
    if not group: return {"error": "Группа не найдена"}

    if group.creator_id != current_user_id:
        return {"error": "Нет прав на редактирование настроек группы"}

    if name is not None:
        group.name = name
    if description is not None:
        group.description = description
        
    db.commit()

    return {"status": "ok", "name": group.name, "description": group.description}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
