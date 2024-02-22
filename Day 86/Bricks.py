from turtle import Turtle

class Brick:
    def __init__(self):
        x = -400
        y = 280
        for i in range(1, 23):
            self.brick = Turtle()
            self.brick.shape("square")
            self.brick.penup()

            self.brick.shapesize(stretch_wid=1, stretch_len=2)
            # brick.setpos((x, y))
            self.brick.teleport(x, y)
            x += 41

        x = -400
        y = 260
        for i in range(1, 23):
            self.red = Turtle()
            self.red.shape("square")
            self.red.penup()
            self.red.color("red")
            self.red.shapesize(stretch_wid=1, stretch_len=2)
            self.red.teleport(x, y)
            x += 41

        x = -400
        y = 240
        for i in range(1, 23):
            self.green = Turtle()
            self.green.shape("square")
            self.green.penup()
            self.green.color("green")
            self.green.shapesize(stretch_wid=1, stretch_len=2)
            self.green.teleport(x, y)
            x += 41

    def return_green(self):
        return self.green.xcor()

    def return_red(self):
        return self.red.xcor()

    def return_black(self):
        return self.brick.xcor()

    def fall(self):
        self.red.hideturtle()



