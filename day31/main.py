from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("day31\\data\\words_to_learn.csv")
    data_french_list = data.to_dict(orient="records")
except FileNotFoundError:
    ori_data = pandas.read_csv("day31\\data\\french_words.csv")
    data_french_list = ori_data.to_dict(orient="records")

random_number = 0
current_card = {}

def generte_random_word():
    canvas.itemconfig(language_text, text="French")
    random_letter = random.randint(0, len(data_french_list))
    global random_number, current_card
    random_number = random_letter
    data_specified = data_french_list[random_letter]
    current_card = data_specified
    french_letter = data_specified["French"]
    canvas.itemconfig(language_text_word, text=french_letter)

def is_known():
    data_french_list.remove(current_card)
    data_dataframe = pandas.DataFrame(data_french_list)
    data_dataframe.to_csv("day31\\data\\words_to_learn.csv", index=False)
    generte_random_word()

def flip_card():
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(language_text, text="English")
    data_in_english = data_french_list[random_number]
    data_specified_english = data_in_english["English"]
    canvas.itemconfig(language_text_word, text=data_specified_english)
    flip_timer = window.after(3000, func=flip_card)

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Language Learning App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas= Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
photo = PhotoImage(file="day31\\images\\card_front.png")
canvas.create_image(400, 263, image=photo)


language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
language_text_word = canvas.create_text(400, 263, text="00:00", fill="black", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

photo_wrong = PhotoImage(file="day31\\images\\wrong.png")
button_wrong = Button(image=photo_wrong, highlightthickness=0, command=generte_random_word)
button_wrong.grid(row=1, column=0)

photo_right = PhotoImage(file="day31\\images\\right.png")
button_right = Button(image=photo_right, highlightthickness=0, command=generte_random_word)
button_right.grid(row=1, column=1)

photo_english = PhotoImage(file="day31\\images\\card_back.png")

generte_random_word()

window.mainloop()