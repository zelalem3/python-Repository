from turtle import Turtle
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(). __init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 260)

    def update_scoreboard(self):
        self.clear()
        self.write(f"level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
