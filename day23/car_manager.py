from turtle import Turtle
from random import randint
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.allcars = []
        self.createcars()

    def createcars(self):
        numberofincrement = randint(1, 6)
        if numberofincrement == 1:
            ujwal = Turtle(shape="square")
            ujwal.shapesize(stretch_wid=1, stretch_len=2)
            ujwal.color(choice(COLORS))
            ujwal.penup()
            ycoor = randint(-250, 250)
            ujwal.goto(300, ycoor)
            self.allcars.append(ujwal)

    def moveback(self):
        for touring in self.allcars:
            touring.backward(STARTING_MOVE_DISTANCE)

    def levelup(self):
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
