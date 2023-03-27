from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("classic")

for _ in range(4):
    tim.forward(100)
    tim.left(90)


#
screen = Screen()
screen.exitonclick()

