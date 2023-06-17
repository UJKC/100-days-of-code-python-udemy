from turtle import Turtle
import random
import turtle

man = Turtle()
turtle.colormode(255)
def sizeofcircle(size):
    for i in range(int(360 / size)):
        man.circle(50)
        man.left(size)
        man.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
sizeofcircle(5)