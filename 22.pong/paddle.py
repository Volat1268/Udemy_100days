from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.speed(0)
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)

    def move_up(self):
        new_ycor = self.ycor() + 20
        self.sety(new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 20
        self.sety(new_ycor)

    def running(self):
        self.forward(10)
        if self.ycor() == 250:
            while self.ycor() > -250:
                self.backward(10)


