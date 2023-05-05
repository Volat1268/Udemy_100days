import time
from turtle import Screen
from player import *
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross the road!")
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.player_move, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            player.go_to_start()
    if player.is_finish_reached():
        player.go_to_start()
        car_manager.change_car_speed()














screen.exitonclick()
