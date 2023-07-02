import tkinter
from exampleclass import example

window = tkinter.Tk()
window.title("Example")
window.minsize(600, 600)

#Label
mylabel = tkinter.Label(text="HI", font=("Arial", 24,"bold"))
mylabel.pack()

#example class
ujwal = example(make="Nissan", model="GTR")
print(ujwal.make)
print(ujwal.model)

#Unlimited addition
def calculate(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)
calculate(1, 2, 3, 4, 5)

window.mainloop()