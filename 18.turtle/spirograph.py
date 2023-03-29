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
tim.pensize(20)
nmb_horiz = 10
nmb_vert = 10

tim.hideturtle()
tim.penup()
tim.setpos(-300, -300)


tim.showturtle()
tim.pendown()
tim.dot(20)
# tim.forward(100)











screen = Screen()
screen.exitonclick()
