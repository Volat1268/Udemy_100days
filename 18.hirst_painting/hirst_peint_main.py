import turtle
from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    current_color = (r, g, b)
    return current_color


colors_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
               (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
               (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
               (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
               (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124),
               (153, 202, 227), (48, 69, 71), (131, 128, 121), (246, 245, 243), (233, 239, 246), (246, 239, 242),
               (240, 246, 243), (132, 166, 205), (221, 148, 106)]

turtle.colormode(255)
tim = Turtle()
tim.hideturtle()
nmb_horiz = 20
nmb_vert = 20
dot_size = 20
step_size = 30
tim.speed("fastest")
tim.penup()
x_pos = -250
y_pos = -250
tim.setpos(x_pos, y_pos)


for y in range(nmb_vert):
    for x in range(nmb_horiz):
        # dot_color = random.choice(colors_list)
        dot_color = random_color()
        tim.dot(dot_size, dot_color)
        tim.forward(step_size)
    y_pos += step_size
    tim.setpos(x_pos, y_pos)


screen = Screen()
screen.exitonclick()
