from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __int__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    def move(self):
        for seg_Num in range(len(self.segments)-1, 0, -1):
            new_X = self.segments[seg_Num-1].xcor()
            new_y = self.segments[seg_Num-1].ycor()
            self.segments[seg_Num].goto(new_X, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def Up(self):
        self.segment[0].setheading(90  )