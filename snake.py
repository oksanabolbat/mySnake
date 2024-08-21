from turtle import Turtle

STEP = 20
STARTING_COORS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        turtle_segment = Turtle("square")
        turtle_segment.color("#fff")
        turtle_segment.penup()
        turtle_segment.goto(position)
        self.segments.append(turtle_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def create_snake(self):
        for position in STARTING_COORS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
