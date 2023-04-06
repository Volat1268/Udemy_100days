from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


segments = []
start_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in start_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
# while game_is_on:
#     for seg in segments:
#         seg.penup()
#         seg.fd(20)

while game_is_on:
    screen.update()
    time.sleep(1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].fd(20)





screen.exitonclick()
