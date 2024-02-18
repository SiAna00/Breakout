from turtle import *


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

# Create paddle
paddle = Turtle()
paddle.up()
paddle.goto(0, -270)
paddle.shape("square")
paddle.shapesize(stretch_wid=None, stretch_len=5, outline=None)
paddle.color("white")
screen.tracer(0)

screen.onkeypress(move_paddle_right, "Right")
screen.onkeypress(move_paddle_left, "Left")
screen.listen()

screen.exitonclick()