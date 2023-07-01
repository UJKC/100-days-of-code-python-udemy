from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        with open(file="file.txt", mode="r") as file:
            self.highscore = file.read()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        if self.score > self.highscore:
            with open(file="file.txt", mode="w") as file:
                file.write(f"{self.score}")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
