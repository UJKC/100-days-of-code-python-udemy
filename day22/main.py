from turtle import Screen
from paddle import Paddle
from ball import Ball
from mid import Midline
from scoreboard import Score

gameison = True

screen = Screen()
skore = Score()
screen.title("Pong")
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("Black")
team1 = Paddle(-350, 0)
team2 = Paddle(350, 0)
midline = Midline()
paintball = Ball()
screen.listen()
screen.onkey(team1.moveup, key="w")
screen.onkey(team1.movedown, key="s")
screen.onkey(team2.moveup, key="Up")
screen.onkey(team2.movedown, key="Down")
while gameison:
    screen.update()
    paintball.move()
    if paintball.ycor() > 280 or paintball.ycor() < -280:
        paintball.ultapaintaballtowardsyaxis()
    if (paintball.distance(team1) < 80 and paintball.xcor() < -350) or (paintball.distance(team2) < 80 and paintball.xcor() < 350):
        paintball.ultapaintaballtowardsxaxis()
    if paintball.xcor() < -380:
        paintball.resetposition()
        skore.increment_team2()
    if paintball.xcor() > 380:
        paintball.resetposition()
        skore.increment_team1()
screen.exitonclick()