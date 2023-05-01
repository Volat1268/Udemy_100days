from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_change = 10
        self.y_change = 10

    def move(self):
        new_xcor = self.xcor() + self.x_change
        new_ycor = self.ycor() + self.y_change
        self.goto(new_xcor, new_ycor)

    def y_bonce(self):
        self.y_change *= -1

    def x_bonce(self):
        self.x_change *= -1





