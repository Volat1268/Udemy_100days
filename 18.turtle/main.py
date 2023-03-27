from turtle import Turtle, Screen
import random

tim = Turtle()
colours = [
    "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]
angles = [
    0, 90, 180, 270
]


tim.pensize(5)
tim.ht()
tim.speed(30)
# for _ in range(50):
#     x = random.randint(0, 200)
#     y = random.randint(0, 200)
#     tim.setx(x)
#     tim.sety(y)


for _ in range(200):
    pen_color = random.choice(colours)
    angle = random.choice(angles)
    # angle = random.randint(0, 360)
    tim.forward(30)
    tim.setheading(angle)
    tim.pencolor(pen_color)




















screen = Screen()
screen.exitonclick()

