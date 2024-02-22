from turtle import Screen, Turtle
import math
import time
from ball import Ball
from Bricks import Brick
from score_board import Scoreboard

def move_left():
    paddle.setx(paddle.xcor() - 20)

def move_right():
    paddle.setx(paddle.xcor() + 20)




screen = Screen()
screen.setup(width=800, height=590)
screen.listen()
screen.onkey(move_left,"Left")
screen.onkey(move_right, "Right")
paddle = Turtle()
paddle.shape("square")
paddle.color("black")
paddle.penup()
paddle.goto(0, -270)
paddle.shapesize(stretch_wid=1, stretch_len=5)
ball = Ball()
brick = Brick()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    ball.move()
    if ball.ball.ycor() < -270:
        game_is_on = False
        scoreboard.gameover()

    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.bounce_y()

    if ball.ball.xcor() > 340 and ball.ball.distance(paddle) < 50:
        ball.bounce_y()

    if ball.ball.distance(paddle) < 50 and ball.ball.ycor() < -250:
        ball.bounce_y()

    if ball.ball.xcor() > 390 or ball.ball.xcor() < -390:
        ball.bounce_x()
    if ball.ball.distance(brick) > 50:
        ball.bounce_y()


screen.mainloop()