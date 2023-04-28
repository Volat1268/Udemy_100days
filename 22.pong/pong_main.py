from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("My Pong game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    # l_paddle.running()








screen.exitonclick()
