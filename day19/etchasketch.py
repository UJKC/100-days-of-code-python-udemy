from turtle import Turtle, Screen

me = Turtle()
def move_forward():
    me.forward(50)
def move_backward():
    me.backward(50)
def turn_left():
    me.left(10)
def turm_right():
    me.right(10)
def move_to_home():
    me.clear()
    me.penup()
    me.home()
    me.pendown()
sceen = Screen()
sceen.exitonclick()
sceen.listen()
sceen.onkey(move_forward, "W")
sceen.onkey(move_backward, "S")
sceen.onkey(turn_left, "A")
sceen.onkey(turm_right, "D")
sceen.onkey(move_to_home, "C")