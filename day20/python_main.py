import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Turtle_class:
    def __init__(self):
        self.allsnakes = []
        self.createsnake()
        self.head = self.allsnakes[0]
        self.move()

    def createsnake(self):
        for start in STARTING_POSITIONS:
            man = t.Turtle(shape='square')
            man.color('white')
            man.penup()
            man.goto(start)
            self.allsnakes.append(man)

    def move(self):
        for segment in range(len(self.allsnakes) -1, 0, -1):
            xcoor = self.allsnakes[segment -1].xcor()
            ycoor = self.allsnakes[segment -1].ycor()
            self.allsnakes[segment].goto(xcoor, ycoor)
        self.head.forward(20)

    def moveup(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def movedown(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def moveleft(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def moveright(self):
        if self.head.heading() != 180:
            self.head.setheading(0)