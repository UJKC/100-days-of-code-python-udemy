from tkinter import *
from exampleclass import example

def clicked():
    print("I got clicked")
    dumy = input.get()
    mylabel.config(text=dumy)

window = Tk()
window.title("Example")
window.minsize(600, 600)

#Label
mylabel = Label(text="HI", font=("Arial", 24,"bold"))
mylabel.pack()

#Button
myButton = Button(text="Hit Me", background="yellow", font=("Arial", 24,"bold"), command=clicked)
myButton.pack()

#Entry
input = Entry(width=24)
input.pack()

window.mainloop()