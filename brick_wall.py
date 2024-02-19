from turtle import Turtle

class BrickWall():
    def __init__(self):
        self.bricks = []
        start_pos_x = -280
        start_pos_y = 240

        for i in range(15):
            new_brick = Turtle()
            new_brick.up()
            new_brick.shape("square")
            new_brick.shapesize(stretch_wid=None, stretch_len=2)
            new_brick.color("black", "red")
            new_brick.goto(start_pos_x + i * 40, start_pos_y)
            self.bricks.append(new_brick)