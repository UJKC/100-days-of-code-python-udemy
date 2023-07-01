import python_main as tm
import time as ti
from turtle import Screen
import food as food
from scoremyass import Scoreboard

playing = True
ujwal = tm.Turtle_class()
food = food.food()
score = Scoreboard()
screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)
screen.listen()
screen.title("My Snake Game")
screen.tracer(0)
screen.onkey(fun=ujwal.moveup, key='Up')
screen.onkey(fun=ujwal.movedown, key='Down')
screen.onkey(fun=ujwal.moveleft, key='Left')
screen.onkey(fun=ujwal.moveright, key='Right')
while playing:
    screen.update()
    ujwal.move()
    ti.sleep(0.1)
    if ujwal.head.distance(food) < 15:
        food.refreshfood()
        score.increase_score()
        ujwal.extend()
    if ujwal.head.xcor() > 280 or ujwal.head.xcor() < -280 or ujwal.head.ycor() > 280 or ujwal.head.ycor() < -280:
        playing = False
    for segment in ujwal.allsnakes:
        if segment == ujwal.head:
            pass
        elif ujwal.head.distance(segment) < 10:
            game_is_on = False

screen.exitonclick()