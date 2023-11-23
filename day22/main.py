from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
paddle = Paddle()

r_paddle = paddle((350, 0))
l_Paddle = paddle((-350, 0))


# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

# screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")
game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()
