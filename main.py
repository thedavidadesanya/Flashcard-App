from pandas.core.interchange.dataframe_protocol import DataFrame
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

#------------- FLASH Card ---------------------------

#------------ UI ------------------------------------------

window = Tk()
window.title("FlashCard Doro")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=img)
title_id = canvas.create_text(400, 150, text="French", font=("Ariel", 40,"italic"))
word_id = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

my_button= Button(image=img, highlightthickness=0)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command= french_list)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command= test)
wrong_button.grid(column=0, row=1)






window.mainloop()