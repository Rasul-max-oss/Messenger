from tkinter import *
from datetime import datetime
import random
import os

# Liorpolikarpov

def generate_new_number():
    """Создаёт новую капчу из 5 случайных цифр"""
    global random_number, start_time
    random_number = ''.join(str(random.choice(numbers)) for _ in range(5))
    lable_number.config(text=random_number)
    start_time = datetime.now()


def check_input(event=None):
    """Проверяет введённую капчу и записывает результат"""
    user_input = entry_kapca.get()
    time_taken = (datetime.now() - start_time).total_seconds()

    if user_input == random_number:
        result = "Правильно"
        lable_time.config(text=f"Введено за {time_taken:.2f} сек.")
    else:
        result = "Неверно"
        lable_time.config(text=f"Неверно, введено за {time_taken:.2f} сек.")

    # Запись в файл
    with open("kapcha_time.txt", "a", encoding="utf-8") as file:
        file.write(
            f"Сгенерированная капча: {random_number}, "
            f"Введено: {user_input}, "
            f"Результат: {result}, "
            f"Время: {time_taken:.2f} сек.\n"
        )

    entry_kapca.delete(0, END)
    generate_new_number()


def show_Progress():
    progress_window = Toplevel(window)
    progress_window.title("Прогресс по капче")
    progress_window.geometry("500x500")
    progress_window.config(bg="#B8B8B8")

    def close():
        progress_window.destroy()

    def highlight_best_time():
        """Находит и выделяет самое лучшее (минимальное) время"""
        if not os.path.exists("kapcha_time.txt"):
            return

        with open("kapcha_time.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Извлекаем все времена (в секундах)
        times = []
        for line in lines:
            if "Время:" in line:
                try:
                    t = float(line.strip().split("Время:")[1].replace("сек.", "").strip())
                    times.append(t)
                except:
                    pass

        if not times:
            return

        best_time = min(times)

        # Очистить выделения
        text_box.tag_delete("highlight")
        text_box.tag_config("highlight", background="yellow", foreground="black")

        # Найти строку с лучшим временем и подсветить её
        start_index = "1.0"
        while True:
            pos = text_box.search(f"{best_time:.2f} сек.", start_index, stopindex=END)
            if not pos:
                break
            end_pos = f"{pos} lineend"
            text_box.tag_add("highlight", pos, end_pos)
            start_index = end_pos

    def highlight_worst_time():
        """Находит и выделяет самое худшее (максимальное) время"""
        if not os.path.exists("kapcha_time.txt"):
            return

        with open("kapcha_time.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        times = []
        for line in lines:
            if "Время:" in line:
                try:
                    t = float(line.strip().split("Время:")[1].replace("сек.", "").strip())
                    times.append(t)
                except:
                    pass

        if not times:
            return

        worst_time = max(times)

        text_box.tag_delete("highlight")
        text_box.tag_config("highlight", background="red", foreground="white")

        start_index = "1.0"
        while True:
            pos = text_box.search(f"{worst_time:.2f} сек.", start_index, stopindex=END)
            if not pos:
                break
            end_pos = f"{pos} lineend"
            text_box.tag_add("highlight", pos, end_pos)
            start_index = end_pos

    Label(progress_window, text="История капчи:", font=("Arial", 14, "bold"),
          bg="#B8B8B8", fg="black").pack(pady=10)

    text_box = Text(progress_window, wrap=WORD, bg="#2B2B2B", fg="white",
                    font=("Consolas", 10))
    text_box.pack(expand=True, fill=BOTH, padx=10, pady=10)

    # Кнопки внизу справа и слева
    frame_buttons = Frame(progress_window, bg="#B8B8B8")
    frame_buttons.pack(fill=X, pady=5)

    btn_destroy = Button(frame_buttons, text="X", font="Arial 14 bold",
                         fg="black", bg="White", command=close)
    btn_destroy.pack(side=LEFT, padx=10)

    btn_worse = Button(frame_buttons,text="Худщее время",fg="White",bg="Red",font="Arial 14 bold",command=highlight_worst_time)
    btn_worse.pack(side=RIGHT,padx=5)

    btn_thebest = Button(frame_buttons, text="Лучшее время", bg="#24FA14",
                         font="Arial 14 bold", fg="black", command=highlight_best_time)
    btn_thebest.pack(side=RIGHT, padx=10)

    # Показ содержимого файла
    if os.path.exists("kapcha_time.txt"):
        with open("kapcha_time.txt", "r", encoding="utf-8") as file:
            content = file.read()
            text_box.insert(END, content)
    else:
        text_box.insert(END, "Пока нет данных. Пройдите капчу, чтобы появились результаты.")

    text_box.config(state=DISABLED)



window = Tk()
window.title("Капча ввод")
window.geometry("270x250")
window.resizable(False, False)
window.config(bg="#B8B8B8")

numbers = list(range(10))
random_number = ''
start_time = None

Frame_vvod = Frame(window, bg="#999999")
Frame_vvod.pack(pady=10, padx=10)

lable_number = Label(Frame_vvod, text="", bg="#2B2B2B", fg="white", font=("Arial", 24))
lable_number.pack(pady=10)

entry_kapca = Entry(Frame_vvod, bg="#2B2B2B", fg="#0092D9", font=("Arial", 14))
entry_kapca.pack(pady=8)
entry_kapca.bind('<Return>', check_input)

button_sent = Button(Frame_vvod, text="Проверить", command=check_input, bg="#2B2B2B", fg="White")
button_sent.pack(pady=5)

lable_time = Label(Frame_vvod, text="Введите капчу", bg="#999999", fg="black", font=("Arial", 10))
lable_time.pack(pady=5)

btn_progress = Button(window, text="Посмотреть прогресс",
                      bg="#8F8F8F", fg="Black", font="Arial 12 bold",
                      command=show_Progress)
btn_progress.pack(pady=10)

generate_new_number()
window.mainloop()