# Uses the modules turtle & random
from turtle import Turtle
import random

# Inherits from the turtle class and is called every time the "food" is eaten.


class Food(Turtle):

    # Controls the creation and graphics of the food.
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # Randomly determines its position on the screen.
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
