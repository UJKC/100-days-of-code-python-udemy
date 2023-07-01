from turtle import Turtle

class Score(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.hideturtle()
        self.clear()
        self.color("white")
        self.team1 = 0
        self.team2 = 0
        self.update_scoreboard()
        self.shapesize(20)

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 290)
        self.write(f"{self.team1}")
        self.goto(350, 290)
        self.write(f"{self.team2}")

    def increment_team1(self):
        self.team1 += 1
        self.update_scoreboard()

    def increment_team2(self):
        self.team2 += 1
        self.update_scoreboard()