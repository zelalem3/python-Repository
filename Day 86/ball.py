from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.shapesize(stretch_len=1, stretch_wid=1)
        self.ball.color("black")
        self.x = 10
        self.y = 10

    def move(self):
        new_x = self.ball.xcor() + self.x
        new_y = self.ball.ycor() + self.y
        self.ball.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def get_xcor(self):
        return self.ball.xcor()

