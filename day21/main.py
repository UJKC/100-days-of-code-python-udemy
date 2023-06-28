import python_main as tm
import time as ti
from turtle import Screen

playing = True
ujwal = tm.Turtle_class()
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
screen.exitonclick()