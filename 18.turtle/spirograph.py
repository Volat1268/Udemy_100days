import turtle
from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    current_color = (r, g, b)
    return current_color


turtle.colormode(255)


tim = Turtle()
angle = 3
tim.speed(30)
for _ in range(int(360 / angle)):
    pen_color = random_color()
    tim.pencolor(pen_color)
    tim.circle(200)
    tim.right(angle)







screen = Screen()
screen.exitonclick()
