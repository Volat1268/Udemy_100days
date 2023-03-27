import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()

angles = [
    0, 90, 180, 270
]
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    current_color = (r, g, b)
    return current_color


tim.pensize(5)
tim.ht()
tim.speed(30)

for _ in range(200):
    pen_color = random_color()
    angle = random.choice(angles)
    tim.forward(30)
    tim.setheading(angle)
    tim.pencolor(pen_color)




















screen = Screen()
screen.exitonclick()

