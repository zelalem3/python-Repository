from turtle import Screen, Turtle
from paddle import Paddle
paddle = Paddle()

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

r_paddle = paddle((350, 0))
l_Paddle = paddle((-350, 0))
screen.listen()
screen.onkey(go_up, "up")
screen.onkey(go_down, "up")
game_is_On =True
while game_is_On:
    screen.update()



screen.exitonclick()
