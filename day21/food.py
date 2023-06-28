import turtle as ttfood
import random as rf

class food(ttfood.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.penup()
        self.refreshfood()

    def refreshfood(self):
        self.goto(x=rf.randint(-280, 280), y=rf.randint(-280, 280))