from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.pose_scoreboard()

    def pose_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def change_scoreboard(self):
        self.clear()
        self.score += 1
        self.pose_scoreboard()






