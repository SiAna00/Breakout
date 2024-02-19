import random
from turtle import *
from ball import Ball
from brick_wall import BrickWall
from paddle import Paddle
from score import ScoreBoard

# Create screen
screen = Screen()
screen.title("Breakout")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Create score
scoreboard = ScoreBoard()

# Create brick wall
brick_wall = BrickWall()

# Create paddle
paddle = Paddle()

# Create ball
ball = Ball()

# Move paddle on key press
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")
screen.listen()

while True:
    screen.update()
    ball.move()
    
    # Detect collisions with left and right wall
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.step_x *= -1

    # Bounce ball of paddle
    if ball.distance(paddle) <= 20:
        ball.step_y *= -1

    # When ball falls
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.step_x *= -1

    # Detect collision with brick wall
    for brick in brick_wall.bricks:
        if brick.distance(ball) <= 20:
            ball.step_y *= -1
            brick.reset()
            scoreboard.update_score()


        

screen.exitonclick()