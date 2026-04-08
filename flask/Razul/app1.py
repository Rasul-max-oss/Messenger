from tkinter import *
from tkinter import messagebox
from app2 import show


window = Tk()
window.title("dd")
window.geometry("500x500")
window.config(bg="lightyellow")

btn = Button(text="Click",font="Arial 24 bold",bg="lightyellow",command=show)
btn.pack()







window.mainloop()