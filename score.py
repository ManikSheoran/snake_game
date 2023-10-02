from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))
        self.hideturtle()

    def update(self):
        self.write(arg="Score = {self.score}", align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 14, "bold"))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))
