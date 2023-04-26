from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(350, 0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)


