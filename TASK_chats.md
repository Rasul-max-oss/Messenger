# Задание: Реализация страницы "/chats" — Список всех чатов

## Цель
Создать маршрут и страницу для отображения всех чатов текущего пользователя.

---

## Что нужно сделать

### 1. В `main.py` создать маршрут `/chats`

```python
@app.get('/chats')
def chats_page(request: Request, db: Session = Depends(get_db)):
    # Получить user_id из cookies
    # Если нет — редирект на /login_page
    
    # Получить все чаты, где участвует текущий пользователь
    # (user1_id или user2_id == current_user_id)
    
    # Для каждого чата найти собеседника (не текущего пользователя)
    
    # Передать в шаблон: current_user и список chats_with_partner
    return templates.TemplateResponse("chats.html", {...})
```

### 2. Создать файл `templates/chats.html`

**Структура страницы:**
- Заголовок "Мои чаты"
- Кнопка "← Назад в профиль" (ссылка на `/profile`)
- Список чатов (каждый чат — карточка с):
  - Аватар собеседника
  - Имя собеседника
  - Кнопка "Открыть чат" → ссылка на `/chat/{chat_id}`

**Пример HTML-структуры:**
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Мои чаты | Messenger</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        /* Стили в духе profile.html */
        .chat-list { ... }
        .chat-item { ... }
    </style>
</head>
<body>
    <div class="container">
        <a href="/profile" class="btn-back">← Назад в профиль</a>
        <h2>Мои чаты</h2>
        
        {% if chats %}
            {% for chat, partner in chats %}
                <div class="chat-item">
                    <img src="{{ partner.avatar }}" alt="{{ partner.username }}">
                    <span>{{ partner.username }}</span>
                    <a href="/chat/{{ chat.id }}">Открыть чат</a>
                </div>
            {% endfor %}
        {% else %}
            <p>У вас пока нет чатов</p>
        {% endif %}
    </div>
</body>
</html>
```

---

## Подсказки

### Запрос для получения чатов пользователя:
```python
chats = db.query(Chat).filter(
    or_(Chat.user1_id == user_id, Chat.user2_id == user_id)
).all()
```

### Как найти собеседника:
```python
for chat in chats:
    partner_id = chat.user2_id if chat.user1_id == current_user_id else chat.user1_id
    partner = db.query(User).filter(User.id == partner_id).first()
```

---

## Критерии готовности
- [ ] При переходе на `/chats` отображается список всех чатов
- [ ] Для каждого чата показано имя и аватар собеседника
- [ ] Кнопка "Открыть чат" ведёт на страницу чата
- [ ] Если чатов нет — выводится сообщение "У вас пока нет чатов"
- [ ] Работает кнопка "Назад в профиль"
