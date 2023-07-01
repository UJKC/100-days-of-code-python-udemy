from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

gameison = True

screen = Screen()
screen.tracer(0)
skore = Scoreboard()
car = CarManager()
screen.setup(600, 600)
team = Player()
screen.listen()
screen.onkey(team.moveup, key="space")
while gameison:
    time.sleep(0.1)
    screen.update()
    car.createcars()
    car.moveback()
    for cartrouble in car.allcars:
        if cartrouble.distance(team) < 20:
            skore.game_over()
            gameison = False
    if team.ycor() > 280:
        car.levelup()
        skore.increase_level()