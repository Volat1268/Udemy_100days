# Create a snake body
# Move the snake
# Control the snake
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail
# ---------------------------------------------------------------------
from turtle import Screen
from snake import Snake
import time
TIME_SLEEP = 0.2


# ------Screen---------
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=800)
screen.title("Play Snake game!")
screen.bgcolor("black")
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(TIME_SLEEP)
    snake.move_snake()
















screen.exitonclick()