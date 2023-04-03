from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")


def tim_forward():
    tim.forward(30)


screen.listen()
screen.onkey(fun=tim_forward, key="space")




screen.exitonclick()