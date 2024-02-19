from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.goto(0, -270)
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=5)
        self.color("white")

    def move_right(self):
        self.forward(50)

        if self.pos() == (300.00, -270.0):
            self.setx(self.xcor() - 50)

    def move_left(self):
        self.backward(50)

        if self.pos() == (-300.00, -270.0):
            self.setx(self.xcor() + 50)