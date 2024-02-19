import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.setheading(random.randint(225, 315))
        self.shape("circle")
        self.color("white")
        self.step_x = 0.4
        self.step_y = 0.4
    
    def move(self):
        self.goto(self.xcor() - self.step_x, self.ycor() - self.step_y)

