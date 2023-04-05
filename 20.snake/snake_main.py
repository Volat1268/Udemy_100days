from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

tim = Turtle(shape="square")
tim.color("white")

x_pos = 0
for t in range(3):
    white_turtle = Turtle(shape="square")
    white_turtle.color("white")
    white_turtle.setx(x=x_pos)
    x_pos -= 20
# --------------------второй вариант рисования тела змеи----------------
# start_positions = [(0, 0), (-20, 0), (-40, 0)]
# for position in start_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)
# ----------------------------------------------------------------------


screen.exitonclick()
