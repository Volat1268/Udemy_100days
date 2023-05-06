from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1
        self.life = 3
        self.color("blue")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def change_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.color("red")
        self.write("GAME OVER!", align="Center", font=FONT)

    def update_life_score(self):
        self.clear()
        self.write(f"Life: {self.life}", align="Right", font=FONT)

    def decrease_life(self):
        self.life -= 1
        self.update_life_score()

