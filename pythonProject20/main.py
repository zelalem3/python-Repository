from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.exitonclick()
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
for position in STARTING_POSITION:
    new_Segment = Turtle("Square")
    new_Segment.color("white")
    new_Segment.goto(position)
