from turtle import Turtle

class Midline(Turtle):
    
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.dot(3)
        self.goto(0, -280)
        self.hideturtle()