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
		with open("./24.snake-2/data.txt") as data:
			self.heigh_score = int(data.read())
		self.update_scoreboard()


	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score} Heigh score: {self.heigh_score}", align=ALIGNMENT, font=FONT)
		
	
	def reset(self):
		if self.score > self.heigh_score:
			self.heigh_score = self.score
			with open("./24.snake-2/data.txt", mode="w") as data:
				data.write(str(self.heigh_score))
		self.score = 0
		self.update_scoreboard()

		
	def increase_score(self):
		self.score += 1
		self.update_scoreboard()
		

			






