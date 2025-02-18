from pandas.core.interchange.dataframe_protocol import DataFrame
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#------------- FLASH Card ---------------------------

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    """This takes us to the next flashcard to study"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_id, text="French", fill="black")
    canvas.itemconfig(word_id, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """This takes us to the english word of the french word"""
    canvas.itemconfig(title_id, text="English", fill="white")
    canvas.itemconfig(word_id, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=new_img)

def is_known():
    """If the word is known already it's removed from to learn dictionary"""
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn", index=False)
    next_card()
#------------ UI ------------------------------------------

window = Tk()
window.title("FlashCard Doro")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
img = PhotoImage(file="images/card_front.png") #front card
new_img = PhotoImage(file="images/card_back.png") #back card
card_bg = canvas.create_image(400,263, image=img)
title_id = canvas.create_text(400, 150, text="French", font=("Ariel", 40,"italic"))
word_id = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

my_button= Button(image=img, highlightthickness=0)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)


next_card()



window.mainloop()