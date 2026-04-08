# from math import expm1
# from tkinter import *
# from tkinter import messagebox
#
# def main():
#     window = Tk()
#     window.title("Многостраничное приложение")
#     window.geometry("500x500")
#     window.config(bg="lightyellow")
#
#     #Функция для 1 страницы
#
#     def show_main_page():
#         #-frame
#         for frame in [main_frame,second_frame,third_frame]:
#             frame.pack_forget()
#         #show main label
#         main_frame.pack(fill="both",expand=True)
#
#     def show_second_page():
#         for frame in [main_frame,second_frame,third_frame]:
#             frame.pack_forget()
#         second_frame.pack(fill="both",expand=True)
#
#     def show_third_page():
#         for frame in [main_frame,second_frame,third_frame]:
#             frame.pack_forget()
#         third_frame.pack(fill="both",expand=True)
#
#
#     #Главная страница
#     main_frame = Frame(window,bg="lightyellow")
#     Label(main_frame,text="Главная страница",font="Arial 24 bold",bg="lightyellow").pack(pady=50)
#
#     Button(main_frame,text="2 page",font="Arial 24 bold",bg="lightblue",command=show_second_page).pack(pady=20)
#
#     Button(main_frame,text="3 page",font="Arial 24 bold",bg="lightblue",command=show_third_page).pack(pady=10)
#
#     #Вторая страница
#     second_frame = Frame(window,bg="lightgreen")
#     Label(second_frame,text="Вторая страница",font="Arial 24 bold",bg="lightgreen").pack(pady=50)
#
#     Button(second_frame,text="Назад",font="Arial 20",bg="lightcoral",command=show_main_page).pack(pady=20)
#
#     #Третия страница
#     third_frame = Frame(window,bg="red")
#     Label(third_frame,text="Третия страница",font="Arial 24 bold",bg="red").pack(pady=50)
#
#     Button(third_frame,text="назад",font="Arial 20",bg="white",command=show_main_page).pack(pady=50)
#
#     #start main page
#     show_main_page()
#     window.mainloop()
#
# main()

from tkinter import *
from tkinter import messagebox
from multiprocessing.connection import families
window = Tk()
window.title("Многостраничное приложение")
window.geometry("500x700")
window.config(bg="lightyellow")

TITLE_FONT = ("Arial", 28, "bold")
BG_COLOR = "#1e1e2e"
BTN_COLOR = "#3a3a5c"
BTN_HOVER = "#5a5a8a"
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#ff4d88"
BUTTON_FONT = ("Arial", 18, "bold")

def show_main_page():
    for frame in [main_frame,second_frame,third_frame,forth_frame]:
        frame.pack_forget()
    main_frame.pack(fill="both",expand=True)

def show_second_page():
    for frame in [main_frame,second_frame,third_frame,forth_frame]:
        frame.pack_forget()
    second_frame.pack(fill="both",expand=True)

def show_third_page():
    for frame in [main_frame,second_frame,third_frame,forth_frame]:
        frame.pack_forget()
    third_frame.pack(fill="both",expand=True)

def show_4_page():
    for frame in [main_frame,second_frame,third_frame,forth_frame]:
        frame.pack_forget()
    forth_frame.pack(fill="both",expand=True)

def i():
    exit()


#главная страница
main_frame = Frame(window,bg=BG_COLOR)
Label(main_frame, text="🎮 DUNGEON QUEST", font=TITLE_FONT, bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=30)

Button(main_frame,text="Играть",font=BUTTON_FONT,bg=BTN_COLOR,fg=TEXT_COLOR,width=15,command=show_second_page).pack(pady=15)

Button(main_frame,text="Настройки",font=BUTTON_FONT,bg=BTN_COLOR,fg=TEXT_COLOR,width=15,command=show_third_page).pack(pady=15)

Button(main_frame,text="Магазин",font=BUTTON_FONT,bg=BTN_COLOR,fg=TEXT_COLOR,width=15,command=show_4_page).pack( pady=15)

Button(main_frame,text="Выход",font="Arial 14 bold",bg="red",fg=TEXT_COLOR,width=10,command=i).pack( pady=15)

main_frame.pack(fill="both",expand=True)


#Вторая страница

second_frame = Frame(window,bg="black")
Label(second_frame, text="🕹️ УРОВЕНЬ 1: ПЕЩЕРА", font=TITLE_FONT, bg="#000000", fg="#00ff00").pack(pady=50)

Button(second_frame,text="Назад в меню",font=BUTTON_FONT,bg="lightgray",fg=TEXT_COLOR,width=15,command=show_main_page).pack(pady=20)

#Третия страница

third_frame = Frame(window,bg=BG_COLOR)
Label(third_frame, text="⚙️ НАСТРОЙКИ", font=TITLE_FONT, bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=30)

Label(third_frame,text="Яркость экрана",fg=TEXT_COLOR,font="Arial 12 bold",bg=BTN_COLOR).pack(pady=20)

Label(third_frame,text="Громкость музыки",fg=TEXT_COLOR,font="Arial 12 bold",bg=BTN_COLOR).pack(pady=20)

Button(third_frame,text="Назад",font=BUTTON_FONT,bg=BTN_COLOR,fg=TEXT_COLOR,width=15,command=show_main_page).pack(pady=15)

#Четвертая страница

forth_frame = Frame(window,bg="#2a0a4a")

Label(forth_frame, text="🛒 МАГАЗИН", font=TITLE_FONT, bg="#2a0a4a", fg="#ffcc00").pack(pady=30)

Label(forth_frame,text="Меч - 100 монет",fg=TEXT_COLOR,font="Arial 12 bold",bg="#2a0a4a").pack(pady=20)
Label(forth_frame,text="броня - 200 монет",fg=TEXT_COLOR,font="Arial 12 bold",bg="#2a0a4a").pack(pady=10)
Label(forth_frame,text="лук - 250 монет",fg=TEXT_COLOR,font="Arial 12 bold",bg="#2a0a4a").pack(pady=10)

Button(forth_frame,text="Buy",font=BUTTON_FONT,bg="yellow",fg="black").pack(pady=10)

Button(forth_frame,text="Назад",font=BUTTON_FONT,bg=BTN_COLOR,fg="white",command=show_main_page).pack(pady=15)




window.mainloop()




