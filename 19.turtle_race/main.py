from turtle import Turtle, Screen
import random

screen = Screen()

width_screen = 800
height_screen = 600
screen.setup(width=width_screen, height=height_screen)
colors = ["red", "blue", "green", "orange", "yellow", "grey", "black"]

nmb_of_turtles = 7
distance_between_turtles = 50
width_of_track = nmb_of_turtles * distance_between_turtles

start = Turtle()
start.ht()
finish = Turtle()
finish.ht()

# start and finish coordinates:
x_start_line = -width_screen / 2 + 50
x_finish_line = -x_start_line
y_north = width_of_track / 2
y_south = -y_north
x_start_turtle = x_start_line - 15
y_first_turtle = - width_of_track / 2 + 30



def draw_line(line, color_line, x):
    """line: start or finish, color_line: color of line, x: x_coordinate of line"""
    line.penup()
    line.color(color_line)
    line.goto(x, y_north)
    line.pendown()
    line.goto(x, y_south)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

draw_line(start, "green", x_start_line)
draw_line(finish, "red", x_finish_line)

turtles = []

for t in range(nmb_of_turtles):
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(colors[t])
    new_turtle.goto(x=x_start_turtle, y=y_first_turtle)
    y_first_turtle += distance_between_turtles

if user_bet:
    is_continue = True

while is_continue:
    for turtle in turtles:
        if turtle.xcor() >= x_finish_line - 15:
            is_continue = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} is winner! ")
            else:
                print(f"You've lose! The {winner} is winner! ")
        distance = random.randint(1, 10)
        turtle.fd(distance)










screen.exitonclick()