import tkinter as tk
from random import randint, choice
from tkinter import messagebox


def add_idea():
    """Adds and writes ideas to a file. Checks for an empty input value."""
    value = EnterText.get()
    if value != "":
        with open("How.txt", "a+", encoding="utf-8") as file:
            file.write(value + "\n")
        EnterText.delete(0, "end")
    else:
        tk.messagebox.showinfo("Error", ("The input field is empty!"))


def random_idea():
    """Generates a random idea from our file"""
    with open("How.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        tk.messagebox.showinfo("Idea", (choice(lines)))

def click_enter():
    add_idea()

window = tk.Tk()

window.resizable(width=False, height=False)
window.title("Idea's generator")
window.geometry("800x400")


window["bg"] = "#fc8c03"

idea = tk.Label(window, text="Add idea", font=("Arial Bold", 15), fg="lime", bg="black")
idea.place(x=350, y=25)
EnterText = tk.Entry(fg="black", width=47)
EnterText.place(x=200, y=65)

btn = tk.Button(
    window, text="Add", command=add_idea, width=40, height="2", fg="black", bg="white"
)
btn.place(x=220, y=110)

window.bind('<Return>', click_enter)

GiveIdeia = tk.Label(
    window, text="Generate an idea", font=("Arial Bold", 15), fg="lime", bg="black"
)
GiveIdeia.place(x=320, y=170)

btn = tk.Button(
    window,
    text="Show idea",
    command=random_idea,
    width=40,
    height="2",
    fg="black",
    bg="white",
)
btn.place(x=220, y=210)

window.mainloop()
