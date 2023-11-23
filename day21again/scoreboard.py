from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        
        self.goto(0, 260)
        self.write(f"score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score}", align="center", font=("courier", 24, "normal"))
    # def end_game(self):
    #     self.color("white")
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("courtier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write(f"score: {self.high_score}", align="center", font=("courier", 24, "normal"))
            self.score = 0
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
