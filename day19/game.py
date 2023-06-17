from turtle import Turtle, Screen
import random
import turtle


race_on = False
screen = Screen()
screen.setup(500, 500)
user_input = screen.textinput("Your bet", "Place your bet: ")
turtle.colormode(255)
number_input = int(input("Enter the number of players: "))
for 