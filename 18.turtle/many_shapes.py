from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("classic")


# colors = [
#     "medium spring green", "gold", "orange red", "yellow green", "rosy brown", "blue3", "black", "DarkOrange3",
#     "HotPink1", "gray10", "LightPink", "HotPink2", "LightSeaGreen", "red", "yellow", "black", "salmon1",
#     "yellow4", "purple3", "snow3", "turquoise", "YellowGreen", "tan1", "LimeGreen"
# ]

colors = [
    "yellow", "black", "red", "blue", "green"
]

def draw_shapes(start_shape, finish_shape):
    angle = start_shape
    for i in range(finish_shape - start_shape + 1):
        current_color = random.choice(colors)
        for _ in range(angle):
            tim.pencolor(current_color)
            tim.forward(100)
            tim.right(360 / angle)
        angle += 1


draw_shapes(3, 10)



screen = Screen()
screen.exitonclick()

