import turtle
from turtle import Turtle, Screen

sketch = Turtle()
screen = Screen()
screen.listen()



def sketch_forwards():
    return sketch.forward(10)


def sketch_backwards():
    return sketch.backward(10)


def sketch_counter_clockwise():
    return sketch.left(10)


def sketch_clockwise():
    return sketch.right(10)


def sketch_clear():
    sketch.clear()
    sketch.penup()
    sketch.home()
    sketch.pendown()



screen.onkeypress(fun=sketch_forwards, key="w")
screen.onkeypress(fun=sketch_backwards, key="s")
screen.onkeypress(fun=sketch_counter_clockwise, key="a")
screen.onkeypress(fun=sketch_clockwise, key="d")
screen.onkey(fun=sketch_clear, key="c")










screen.exitonclick()
