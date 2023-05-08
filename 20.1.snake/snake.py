from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.three_segments = []
        self.create_snake()
        self.snake_head = self.three_segments[0]

    def create_snake(self):
        for position in START_POS:
            one_segment = Turtle("square")
            one_segment.penup()
            one_segment.color("white")
            one_segment.goto(position)
            self.three_segments.append(one_segment)

    def move_snake(self):
        for segment_num in range(len(self.three_segments) - 1, 0, -1):
            new_xcor = self.three_segments[segment_num - 1].xcor()
            new_ycor = self.three_segments[segment_num - 1].ycor()
            self.three_segments[segment_num].goto(new_xcor, new_ycor)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
