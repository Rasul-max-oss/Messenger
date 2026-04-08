from flask import Flask,render_template,request
from tkinter import messagebox
from ast import Index
from tkinter import *


app = Flask(__name__)


@app.route('/opros', methods=['GET', 'POST'])
def opros():
    message = ""  # переменная должна быть внутри функции
    if request.method == "POST":
        name = request.form.get("name")
        school = request.form.get("school")
        why = request.form.get("why")

        message="Данные успешно добавлены!"


        if not name or not school or not why:
            message = "Все ячейки должны быть заполнены!"
            return render_template("opros.html", message=message)



        window = Tk()
        window.title("Ваша статистика опроса")
        window.geometry("400x500")
        window.config(bg="#ED6A51")
        window.resizable(False, False)


        label = Label(window, text=f"Ваше имя и фамилия:\n {name}", font="Helvetica 18 bold", bg="#ED6A51",fg="White")
        label.pack(pady=20)
        label_2 = Label(window, text=f"Ваше мнение о школе:\n {school}", font="Helvetica 18 bold", bg="#ED6A51",fg="White")
        label_2.pack(pady=10)
        label_3 = Label(window, text=f"Почему вы так думаете:\n {why}", font="Helvetica 18 bold", bg="#ED6A51", wraplength=350,fg="White")
        label_3.pack(pady=10)

        btn = Button(window, text="Закрыть", width=15, height=2, font="Helvetica 16 bold", command=window.destroy)
        btn.pack(pady=30)

        window.mainloop()

        # Сохраняем данные в файл
        with open("Opros.txt", "a", encoding="utf-8") as file:
            file.write(name + "\n")
            file.write(school + "\n")
            file.write(why + "\n")

    return render_template("opros.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)
































