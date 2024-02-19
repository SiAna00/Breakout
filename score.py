from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(-280, 270)
        self.color("white")
        self.write(f"Score: {self.score}", align="left", font=("Arial", 14, "bold"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Arial", 14, "bold"))