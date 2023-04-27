from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("My Pong game")
screen.listen()

paddle_right = Paddle()
paddle_left = Paddle()
paddle_left.goto(-350, 0)

screen.onkey(paddle_left.move_up, "Up")
screen.onkey(paddle_left.move_down, "Down")


game_is_on = True
while game_is_on:
    paddle_right.running()








screen.exitonclick()
