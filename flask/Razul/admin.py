import time
from tkinter import *
from tkinter import messagebox, simpledialog

def admin_portal():
    window = Tk()
    window.title("Bank app")
    window.geometry("400x400")
    window.resizable(False, False)
    window.config(bg="#1e1e2f")

    balance = 100000
    balance_2 = 50000
    balance_3 = 10000

    def update_listbox():
        admin_listbox.delete(0, END)
        admin_listbox.insert(END, f"Миша - баланс: {balance}")
        admin_listbox.insert(END, f"Лиор - баланс: {balance_2}")
        admin_listbox.insert(END, f"Расул - баланс: {balance_3}")

    def edit_name():
        try:
            selected_name = admin_listbox.curselection()[0]
            old_name = admin_listbox.get(selected_name)
            new_name = simpledialog.askstring("Редактировать задачу","Изменить имя и баланс:", initialvalue=old_name)
            if new_name:
                admin_listbox.delete(selected_name)
                admin_listbox.insert(selected_name, new_name)
        except IndexError:
            messagebox.showwarning("Ничего не выбрано", "Выберите пользавателя для редактирования!")

    def add():
        global balance, balance_2, balance_3
        try:
            selected_user = admin_listbox.curselection()[0]
            amount = simpledialog.askfloat("Добавить деньги", "Введите сумму для добавления:")
            if amount is None:
                return  # Отмена
            if amount < 0:
                messagebox.showerror("Ошибка", "Нельзя добавить отрицательное число!")
                return

            if selected_user == 0:
                balance += amount
            elif selected_user == 1:
                balance_2 += amount
            elif selected_user == 2:
                balance_3 += amount

            update_listbox()
        except IndexError:
            messagebox.showwarning("Ничего не выбрано", "Выберите пользователя для пополнения!")

    def take():
        global balance,balance_2,balance_3
        try:
            selected_users = admin_listbox.curselection()[0]
            money = simpledialog.askfloat("Снять деньги", "Введите сумму для снятия:")
            if money is None:
                return
            if money<0:
                messagebox.showerror("Ошибка", "Нельзя снять отрицательное число!")
                return

            if selected_users == 0:
                balance -= money
            elif selected_users == 1:
                balance_2 -= money
            elif selected_users==2:
                balance_3 -= money

            update_listbox()
        except IndexError:
            messagebox.showwarning("Ничего не выбрано", "Выберите пользователя для пополнения!")


    Label(window,text="Вы попали в админ зону!")

    clients = [f"Миша - баланс: {balance}",
               f"Лиор - баланс: {balance_2}",
               f"Расул - баланс: {balance_3}"]
    admin_listbox = Listbox(window,width=40,height=10,font="Helvetica 12 bold",bd=3,selectbackground="#0039b3",activestyle="none")
    admin_listbox.pack(pady=10)

    frame_btn = Frame(window,bg="#1e1e2f")
    frame_btn.pack(pady=10)

    Button(frame_btn,text="Добавить",bg="#0BAD00",fg="White",font="Helvetica 14 bold",command=add).pack(side=LEFT,padx=8)
    Button(frame_btn,text="Снять",bg="#B50000",fg="Black",font="Helvetica 14 bold",command=take).pack(padx=8,side=RIGHT)
    Button(frame_btn,text="Изменить аккаунт",bg="#CCE000",fg="Black",font="Helvetica 10 bold",width=15,height=6,command=edit_name).pack(padx=8)

    for client in clients:
        admin_listbox.insert(END,client)




    update_listbox()
    window.mainloop()