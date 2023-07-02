from tkinter import *

def convertmi_km():
    mi = int(input.get())
    km = mi * 1.6
    myanswer.config(text=f"{km}")

window = Tk()
window.minsize(600, 600)
window.title("Enter the Measurement")
window.config(padx=20, pady=50)

mymiles = Label(text="Enter the Miles", font=("Times New Roman", 12, "italic"), background="blue")
mymiles.grid(row=2, column=2)

input = Entry()
input.grid(row=4, column=3)

mybutton = Button(text="Click to Convert", command=convertmi_km, background="green")
mybutton.grid(row=6, column=2)

myanswer = Label(text="Answer", font=("Arial", 12, "bold"))
myanswer.grid(row=8, column=3)

window.mainloop()