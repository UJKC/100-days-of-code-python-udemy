from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 1

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def starttimer():
    global COUNT_ass
    COUNT_ass += 1
    if COUNT_ass == 1 or COUNT_ass == 3 or COUNT_ass == 5 or COUNT_ass == 7:
        times = WORK_MIN
    elif COUNT_ass == 2 or COUNT_ass == 4 or COUNT_ass == 6:
        times = SHORT_BREAK_MIN
    else:
        times = LONG_BREAK_MIN
    count(times * 60)

def stoptimer():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count(time):
    if time >= 0:
        minutes = math.floor(time / 60)
        sec = math.floor(time % 60)
        if sec < 10:
            sec = f"0{sec}"
        canvas.itemconfig(counter, text = f"{minutes}:{sec}")
        window.after(1000, count, time - 1)
    starttimer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
label = Label(text="Timer", fg=GREEN, font=("Arial", 50, "bold"))
label.grid(row=0, column=1)
window.config(padx=50, pady=50, bg=YELLOW)
canvas= Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="day28\\tomato.png")
canvas.create_image(110, 112, image=photo)
counter = canvas.create_text(112, 135, text="00:00", fill="white", font=("Arial", 30, "bold"))
canvas.grid(row=1, column=1)
button = Button(text="Start", command=starttimer, highlightthickness=0, bg=YELLOW)
button.grid(row=2, column=0)
button = Button(text="Reset", command=stoptimer, highlightthickness=0, bg=YELLOW)
button.grid(row=2, column=2)
label = Label(text="✓", fg=GREEN, font=("Arial", 50, "bold"))
label.grid(row=3, column=1)
window.mainloop()