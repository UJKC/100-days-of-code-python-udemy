from turtle import Turtle

class Ball(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.speediny = 3
        self.speeninx = 3
        self.color("white")
        self.penup()
        self.speed(0.1)

    def move(self):
        new_x = self.xcor() + self.speeninx
        new_y = self.ycor() + self.speediny
        self.goto(new_x, new_y)

    def ultapaintaballtowardsyaxis(self):
        self.speediny *= -1

    def ultapaintaballtowardsxaxis(self):
        self.speeninx *= -1
        sting = self.speed() * 0.9
        self.speed(sting)

    def resetposition(self):
        self.goto(0, 0)
        self.ultapaintaballtowardsxaxis()
        self.speed(0.1)
