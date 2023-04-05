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
while game_is_on:
    for seg in segments:
        seg.penup()
        seg.fd(20)
        screen.update()
        time.sleep(1)



screen.exitonclick()
