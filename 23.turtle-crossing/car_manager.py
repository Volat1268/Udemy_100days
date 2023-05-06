from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPEED_INCREMENT = 5
START_XCOR = 290


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        time_for_create_car = random.randint(1, 10)
        if time_for_create_car == 1 or time_for_create_car == 5:
            car = Turtle("square")
            car.penup()
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car_color = random.choice(COLORS)
            car.color(car_color)
            start_ycor = random.randint(-250, 250)
            car.goto(START_XCOR, start_ycor)
            self.all_cars.append(car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def change_car_speed(self):
        self.car_speed += SPEED_INCREMENT

