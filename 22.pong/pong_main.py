from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("My Pong game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

scoreboard = Scoreboard()

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

time_sleep = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.y_bonce()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bonce()

    if ball.xcor() >= 390:
        ball.reset_position()
        scoreboard.l_change()
        scoreboard.scoring()

    if ball.xcor() <= -390:
        ball.reset_position()
        scoreboard.r_change()
        scoreboard.scoring()










screen.exitonclick()
