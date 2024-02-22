from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.rscore = 0
        self.score = Turtle()
        self.score.penup()
        self.score.goto(0, 300)
        self.score.pendown()
        self.score.write(self.rscore, align="center", font=("Arial", 24, "normal"))
    def addblack(self):
        self.score += 4
    def addred(self):
        self.score += 2
    def addgreen(self):
        self.score += 1
    def gameover(self):

        self.score.penup()
        self.score.goto(0,0)
        self.score.pendown()
        self.score.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
        self.score.goto(0, -40)
        self.score.write(f"WITH THE HIGHSCORE OF {self.rscore}", align="center", font=("Arial", 24, "normal"))