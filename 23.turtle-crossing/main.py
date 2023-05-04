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
car_1 = CarManager()
car_2 = CarManager()
# car_4 = CarManager()
# car_5 = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() >= FINISH_LINE_Y:
        print("Finish")









screen.exitonclick()
