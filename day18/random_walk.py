from turtle import *
import random
import turtle

direction = [0, 90, 180, 270]
man = Turtle()
turtle.colormode(255)
man.pensize(10)
while True:
    man.forward(random.randint(-100, 100))
    man.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    man.left(random.choice(direction))
