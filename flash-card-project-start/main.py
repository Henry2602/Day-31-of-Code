from tkinter import *
import pandas as pd
import random

import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
timer = " "
is_word_to_learn = False
try:
    data = pd.read_csv("data/words_to_learn.csv")
    format_data = data.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    format_data = data.to_dict(orient="records")


def new_card():
    global current_card, timer
    window.after_cancel(timer)
    canvas.itemconfig(image, image=front_image)
    canvas.itemconfig(languages_card, fill="black")
    canvas.itemconfig(word_card, fill="black")
    current_card = random.choice(format_data)
    canvas.itemconfig(languages_card, text="French")
    canvas.itemconfig(word_card, text=current_card["French"])
    timer = window.after(ms=3000, func=new_image)


def new_image():
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfig(languages_card, fill="white", text="English")
    canvas.itemconfig(word_card, fill="white", text=current_card["English"])


def is_known():
    format_data.remove(current_card)
    new_card()
    to_learn = pd.DataFrame(format_data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title(string="Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=1, row=1)
languages_card = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_card = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

wrongIconImage = PhotoImage(file="images/wrong.png")
rightIconImage = PhotoImage(file="images/right.png")

wrongButton = Button(image=wrongIconImage, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_card)
wrongButton.grid(column=0, row=2)

rightButton = Button(image=rightIconImage, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
rightButton.grid(column=2, row=2)

new_card()


window.mainloop()
