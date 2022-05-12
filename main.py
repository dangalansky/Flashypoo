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
   original_data = pandas.read_csv('data/countries_capitals.csv')
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
   canvas.itemconfig(card_img, image=card_front)
   canvas.itemconfig(title_text, text='country', fill='black')
   canvas.itemconfig(word_text, text=current_card['country'], fill='black')
   flip_timer = window.after(5000, flip_card)


def flip_card():
   global current_card
   canvas.itemconfig(card_img, image=card_back)
   canvas.itemconfig(title_text, text='capital', fill='white')
   canvas.itemconfig(word_text, text=current_card['capital'], fill='white')


# -------------- GUI ---------------- #
window = Tk()
window.title('Flashypoo: The Flash Card Game')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, flip_card)


# -------------- IMAGES/RESIZING ----------- #
title_open = Image.open('./images/flashy_titl.png')
title_resize = title_open.resize((700, 158), Image.ANTIALIAS)
title = ImageTk.PhotoImage(title_resize)
right_open = Image.open('./images/right.png')
right_resize = right_open.resize((200, 278), Image.ANTIALIAS)
right = ImageTk.PhotoImage(right_resize)
wrong_open = Image.open('./images/wrong.png')
wrong_resize = wrong_open.resize((200, 278), Image.ANTIALIAS)
wrong = ImageTk.PhotoImage(wrong_resize)
cardf_open = Image.open('./images/card_front.png')
cardf_resize = cardf_open.resize((500, 328), Image.ANTIALIAS)
card_front = ImageTk.PhotoImage(cardf_resize)
cardb_open = Image.open('./images/card_back.png')
cardb_resize = cardb_open.resize((500, 328), Image.ANTIALIAS)
card_back = ImageTk.PhotoImage(cardb_resize)
no = PhotoImage(file='./images/no.png')
yup = PhotoImage(file='./images/yup.png')


# -------------- BACKGROUND ----------- #
canvas = Canvas(height=700, width=1000, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(500, 330, image=card_front)
canvas.grid(row=1, column=1)
title_label = Label(image=title, bg=BACKGROUND_COLOR)
title_label.place(x=155, y=0)
no_label = Label(image=no, bg=BACKGROUND_COLOR)
no_label.place(x=5, y=500)
yup_label = Label(image=yup, bg=BACKGROUND_COLOR)
yup_label.place(x=795, y=500)

# ------------- WORDS ----------------- #
title_text = canvas.create_text(495, 260, text='', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(495, 330, text='', font=('Arial', 30, 'bold'))

# ------------ BUTTONS --------------- #
wrong_button = Button(image=wrong, highlightthickness=0, borderwidth=0, bd=0, command=next_card)
wrong_button.place(x=0, y=200)
right_button = Button(image=right, highlightthickness=0, borderwidth=0, command=next_card_know)
right_button.place(x=790, y=200)


next_card()
window.mainloop()


