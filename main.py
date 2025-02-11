from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


#------------ UI ------------------------------------------

window = Tk()
window.title("FlashCard Doro")
window.config(padx=50, pady=50)

canvas = Canvas(height=800, width=800)
img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,400, image=img)
canvas.grid(column=0, row=0, columnspan=2)

my_button= Button(image=img, highlightthickness=0)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)






window.mainloop()