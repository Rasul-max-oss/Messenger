import time
from tkinter import *
from tkinter import messagebox, simpledialog
from admin import admin_portal

def pe():
    window = Tk()
    window.title("Bank app")
    window.geometry("400x600")
    window.resizable(False, False)
    window.config(bg="#1e1e2f")

    # Установка шрифтов
    title_font = ("Helvetica", 18, "bold")
    label_font = ("Helvetica", 12)
    button_font = ("Helvetica", 11, "bold")

    # Начальный баланс
    balance = 15780.50

    # История операций (будем дополнять)
    transaction_history = [
        "21.04.2025 — Пополнение: +5 000,00 ₽",
        "19.04.2025 — Перевод: -2 300,00 ₽",
        "15.04.2025 — Оплата: -1 250,00 ₽",
        "10.04.2025 — Пополнение: +10 000,00 ₽"
    ]




    def history():
        if not transaction_history:
            messagebox.showinfo("История операций", "История пуста.")
        else:
            history_text = "\n".join(transaction_history)
            messagebox.showinfo("История операций", history_text)


    def update_balance_label():
        """Обновляет отображение баланса"""
        balance_label.config(text=f"{balance:,.2f} ₽")


    def check_balance():
        messagebox.showinfo("Баланс", f"Ваш текущий баланс: {balance:,.2f} ₽")


    def deposit():
        global balance
        amount = simpledialog.askfloat("Пополнение", "Введите сумму пополнения:")
        if amount is not None:
            if amount <= 0:
                messagebox.showwarning("Ошибка", "Сумма должна быть больше 0.")
            else:
                balance += amount
                transaction_history.insert(0, f"{time.strftime('%d.%m.%Y')} — Пополнение: +{amount:,.2f} ₽")
                update_balance_label()
                messagebox.showinfo("Успех", f"Счёт пополнен на {amount:,.2f} ₽")


    #Создать функцию трансфер


    def animate_title():
        text = "🏦 MyBank"
        for i in range(len(text) + 1):
            title_label.config(text=text[:i])
            window.update()
            time.sleep(0.2)

    def settings():
        admin_portal()


    def transfer():
        global balance
        simpledialog.askfloat("Перевод","Введите банковский счет другого человека: ")
        amount = simpledialog.askfloat("Перевод","Введите сумму для перевода: ")
        if amount is None:
            return
        if amount <= 0:
            messagebox.showwarning("Ошибка", "Сумма должна быть больше 0.")
            return
        if amount > balance:
            messagebox.showwarning("Ошибка", "Недостаточно средств на счету.")
            return

        balance -= amount
        transaction_history.insert(0, f"{time.strftime('%d.%m.%Y')} — Перевод: -{amount:,.2f} ₽")
        update_balance_label()
        messagebox.showinfo("Успех", f"Вы успешно перевели {amount:,.2f} ₽")



    # Анимированный заголовок
    title_label = Label(window, text="", font=("Helvetica", 20, "bold"),
                        bg="#1e1e2f", fg="#00aaff")
    title_label.pack(pady=30)

    # Подпись "Ваш баланс"
    Label(window, text="Ваш баланс", font=label_font,
          bg="#1e1e2f", fg="#aaaaaa").pack(pady=5)

    # Отображение баланса
    balance_label = Label(window, text=f"{balance:,.2f} ₽", font=("Helvetica", 24, "bold"),
                          bg="#1e1e2f", fg="#ffffff")
    balance_label.pack(pady=10)

    # Кнопка "Просмотреть баланс"
    Button(window, text="Просмотреть баланс", font=button_font,
           bg="#3a3a5c", fg="white", width=20, height=2,
           command=check_balance).pack(pady=10)

    # Кнопки действий
    frame = Frame(window, bg="#1e1e2f")
    frame.pack(pady=20)

    Button(frame, text="💳 Deposit", font=button_font,
           bg="#0088cc", fg="white", width=12, height=2,
           command=deposit).grid(row=0, column=0, padx=10, pady=5)

    Button(frame, text="📤 Transfer", font=button_font,
           bg="#0088cc", fg="white", width=12, height=2,command=transfer
           ).grid(row=0, column=1, padx=10, pady=5)

    Button(frame, text="📋 History", font=button_font,
           bg="#555577", fg="white", width=12, height=2,
           command=history).grid(row=1, column=0, padx=10, pady=5)

    Button(frame, text="⚙️ Settings", font=button_font,
           bg="#555577", fg="white", width=12, height=2,
           command=settings).grid(row=1, column=1, padx=10, pady=5)

    # Запуск анимации после создания окна
    window.after(300, animate_title)




    # Запуск основного цикла
    window.mainloop()
pe()