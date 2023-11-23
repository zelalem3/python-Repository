from turtle import Turtle,Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer()

snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)

    snake.move()









screen.exitonclick()