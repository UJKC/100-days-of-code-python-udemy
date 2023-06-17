from turtle import Turtle, Screen
import random
import turtle

objects = []
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_on = False
screen = Screen()
screen.setup(500, 500)
user_input = screen.textinput("Your bet", "Place your bet: ")
turtle.colormode(255)
for i in range(6):
    man = Turtle(shape='turtle')
    man.color(colors[i])
    objects.append(man)
    man.penup()
    man.goto(-239, y_positions[i])
    man.pendown()
if user_input:
    race_on = True
while race_on:
    for turtle in objects:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()