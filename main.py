import tkinter as tk
from random import randint, choice
from tkinter import messagebox

window = tk.Tk()

window.resizable(width=False, height=False)
window.title("Idea's generator")
window.geometry("800x400")


window["bg"] = "#fc8c03"

idea = tk.Label(window, text="Add idea", font=("Arial Bold", 15), fg="lime", bg="black")
idea.place(x=350, y=25)
EnterText = tk.Entry(fg="black", width=47)
EnterText.place(x=200, y=65)

btn = tk.Button(window, text="Add", width=40, height="2", fg="black", bg="white")
btn.place(x=220, y=110)

GiveIdeia = tk.Label(
    window, text="Generate an idea", font=("Arial Bold", 15), fg="lime", bg="black"
)
GiveIdeia.place(x=320, y=170)

btn = tk.Button(window, text="Show idea", width=40, height="2", fg="black", bg="white")
btn.place(x=220, y=210)

window.mainloop()
