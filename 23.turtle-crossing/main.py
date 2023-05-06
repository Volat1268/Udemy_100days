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
level = Scoreboard()
life_score = Scoreboard()
life_score.goto(260, 260)
life_score.update_life_score()
lives_left = 3

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            lives_left -= 1
            if lives_left > 0:
                player.go_to_start()
                life_score.decrease_life()
            else:
                life_score.decrease_life()
                level.game_over()
                game_is_on = False
    if player.is_finish_reached():
        player.go_to_start()
        car_manager.change_car_speed()
        level.change_level()














screen.exitonclick()
