from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
start_xcor = random.randrange(100, 250)
start_ycor = random.randrange(-250, 250)


class CarManager():
    def __init__(self):
        al_cars = []


