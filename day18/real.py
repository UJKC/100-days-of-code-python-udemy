from turtle import Turtle
import random
import turtle

rock = Turtle()
turtle.colormode(255)
good_color = [(132, 166, 205), (221, 148, 106)]
rock.penup()
rock.setheading(255)
rock.forward(300)
rock.setheading(0)
rock.pendown()
def tank():
    for i in range(10):
        rock.dot(20, random.choice(good_color))
        rock.penup()
        rock.forward(50)
        rock.pendown()
    if rock.heading() == 0:
        rock.setheading(90)
        rock.penup()
        rock.forward(50)
        rock.setheading(180)
        rock.forward(50)
        rock.pendown()
    else:
        rock.setheading(90)
        rock.penup()
        rock.forward(50)
        rock.setheading(0)
        rock.forward(50)
        rock.pendown()
for j in range(10):
    tank()
screem = turtle.Screen()
screem.exitonclick()