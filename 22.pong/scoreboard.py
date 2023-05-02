from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.scoring()

    def scoring(self):
        self.clear()
        self.goto(-50, 230)
        self.write(self.l_score, align="Center", font=("Courier", 25, "bold"))
        self.goto(50, 230)
        self.write(self.r_score, align="Center", font=("Courier", 25, "bold"))

    def l_change(self):
        self.l_score += 1

    def r_change(self):
        self.r_score += 1

