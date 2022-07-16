from tkinter import *
import pandas
import random
from PIL import ImageTk, Image

BACKGROUND_COLOR = "#99C39D"
current_card = {}
to_learn = {}

# ------------ CSV FILE -------------- #
try:
    data = pandas.read_csv('data/capitals_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/us_capitals.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# ------------- NEXT_CARD FUNC() -------------- #
def next_card_know():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('data/capitals_to_learn.csv', index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_img, image=border)
    canvas.itemconfig(title_text, text='state', fill='black')
    canvas.itemconfig(word_text, text=current_card['state'], fill='black')
    flip_timer = window.after(5000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_img, image=border_back)
    canvas.itemconfig(title_text, text='capital', fill='white')
    canvas.itemconfig(word_text, text=current_card['capital'], fill='white')


# -------------- GUI ---------------- #
window = Tk()
window.title('Flashypoo: The Flash Card Game')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, flip_card)

# -------------- IMAGES/RESIZING ----------- #
border_open = Image.open('./images/border.png')
border = ImageTk.PhotoImage(border_open)
border_back_open = Image.open('./images/border_back.png')
border_back = ImageTk.PhotoImage(border_back_open)
title_open = Image.open('./images/flashy_titl.png')
title_resize = title_open.resize((560, 126), Image.ANTIALIAS)
title = ImageTk.PhotoImage(title_resize)
right_open = Image.open('./images/right.png')
right_resize = right_open.resize((160, 222), Image.ANTIALIAS)
right = ImageTk.PhotoImage(right_resize)
wrong_open = Image.open('./images/wrong.png')
wrong_resize = wrong_open.resize((160, 222), Image.ANTIALIAS)
wrong = ImageTk.PhotoImage(wrong_resize)
no = PhotoImage(file='./images/no.png')
no_open = Image.open('./images/no.png')
no_resize = no_open.resize((107, 84), Image.ANTIALIAS)
no = ImageTk.PhotoImage(no_resize)
yup_open = Image.open('./images/yup.png')
yup_resize = yup_open.resize((107, 99), Image.ANTIALIAS)
yup = ImageTk.PhotoImage(yup_resize)

# -------------- BACKGROUND ----------- #
canvas = Canvas(height=600, width=1000, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(500, 300, image=border)
canvas.grid(row=0, column=0)

title_label = Label(image=title, bg=BACKGROUND_COLOR)
title_label.place(x=215, y=20)
no_label = Label(image=no, bg=BACKGROUND_COLOR)
no_label.place(x=60, y=450)
yup_label = Label(image=yup, bg=BACKGROUND_COLOR)
yup_label.place(x=820, y=450)

# ------------- WORDS ----------------- #
title_text = canvas.create_text(495, 270, text='', font=('Helvetica', 20, 'italic'))
word_text = canvas.create_text(495, 330, text='', font=('Helvetica', 30, 'bold'))

# ------------ BUTTONS --------------- #
wrong_button = Button(image=wrong, highlightthickness=0, borderwidth=0, bd=0, command=next_card)
wrong_button.place(x=40, y=200)
right_button = Button(image=right, highlightthickness=0, borderwidth=0, command=next_card_know)
right_button.place(x=790, y=200)

next_card()
window.mainloop()
