# Imports the turtle module.
from turtle import Turtle

# Variables to store the starting position, distance to move & direction.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # Defines the variables for the snake object and the initial function to create the snake.
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creates the initial snake object.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Creates the segments and adds them to a list.
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Resets the position and segments upon a game over condition.
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # Provides the parameters when adding segments to the snake.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Controls how far the snake moves with its segments.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Controls the rotation direction the snake moves in.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
