import time
from tkinter import *
from tkinter import messagebox, simpledialog
from project import pe


window = Tk()
window.title("Login")
window.geometry("400x300")
window.resizable(False, False)
window.config(bg="#1e1e2f")



login_frame = Frame(window,bg="#002BB8")
bank_frame = Frame(window,bg="#1e1e2f")



Label(login_frame,text="Введите имя:",fg="White",bg="#002BB8").pack(pady=10)
entry_name = Entry(login_frame,font="Helvetica 14 bold")
entry_name.pack(pady=5)

Label(login_frame,text="Введите пароль:",fg="White",bg="#002BB8").pack(pady=15)
entry_pas = Entry(login_frame,font="Helvetica 14 bold")
entry_pas.pack(pady=5)


def show_main_page():
    for frame in [login_frame,bank_frame]:
        frame.pack_forget()
    login_frame.pack(fill="both",expand=True)

show_main_page()

################################################

def show_bank_page():
    for frame in [login_frame,bank_frame]:
        frame.pack_forget()
    bank_frame.pack(fill="both",expand=True)

def animate_title():
    text = "🏦 MyBank"
    for i in range(len(text) + 1):
        title_label.config(text=text[:i])
        window.update()
        time.sleep(0.2)


title_label = Label(bank_frame, text="Bank", font=("Helvetica", 20, "bold"),bg="#1e1e2f", fg="#00aaff")
title_label.pack(pady=30)




window.mainloop()

