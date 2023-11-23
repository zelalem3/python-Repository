from turtle import Turtle


class Paddle(Turtle):
    def __Init__(self, position):
        super(). __init__()
        self.shape("square")
        self.penup()
        self.goto(350, 0)
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
