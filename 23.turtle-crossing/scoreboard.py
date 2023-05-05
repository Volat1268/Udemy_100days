from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.create_score()

    def create_score(self):
        self.clear()
        self.goto(-50, 290)
        self.write(self.l_score, align="Center", font=FONT)
        self.goto(50, 290)
        self.write(self.r_score, align="Center", font=FONT)

    def l_score_change(self):
        self.l_score += 1

    def r_score_change(self):
        self.r_score += 1
