from turtle import *
import random


def create_ball():
    ball = Turtle()
    ball.up()
    ball.setheading(random.randint(225, 315))
    ball.goto(0, 0)
    ball.shape("circle")
    ball.color("white")
    return ball


def move_paddle_right():
    paddle.forward(50)
    if paddle.pos() == (300.0, -270.0):
        paddle.goto(paddle.xcor() - 50, paddle.ycor())
    screen.update()


def move_paddle_left():
    paddle.backward(50)
    if paddle.pos() == (-300.0, -270.0):
        paddle.goto(paddle.xcor() + 50, paddle.ycor())
    screen.update()


# Create screen
screen = Screen()
screen.title("Breakout")
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Create brick wall
initial_x = -320
for i in range(15):
    brick = Turtle()
    brick.up()
    brick.goto(initial_x + 40, 280)
    brick.shape("square")
    brick.shapesize(stretch_wid=None, stretch_len=2, outline=None)
    brick.color("red")
    initial_x += 40

# Create paddle
paddle = Turtle()
paddle.up()
paddle.goto(0, -270)
paddle.shape("square")
paddle.shapesize(stretch_wid=None, stretch_len=5, outline=None)
paddle.color("white")

# Create ball
ball = create_ball()

# Move paddle on key press
screen.tracer(0)

screen.onkeypress(move_paddle_right, "Right")
screen.onkeypress(move_paddle_left, "Left")
screen.listen()

# Move ball
step_x = 0.5
step_y = 0.5

while True:
    ball.goto(ball.xcor() - step_x, ball.ycor() - step_y)
    screen.update()

    # Bounce ball of paddle
    if ball.distance(paddle) <= 50:
        """ ball.setheading(-ball.heading()) """
        step_y *= -1

    # Bounce ball of wall
    if ball.xcor() >= 290 or ball.xcor() <= -290:
        step_x *= -1
        
    # Destroy bricks
        if ball.distance(brick) <= 20:
            brick.reset()
            """ if ball.ycor() >= 260: """
            step_y *= -1

    # When ball falls
    if ball.ycor() < -270:
        create_ball()



screen.exitonclick()