# Imports the turtle module.
from turtle import Turtle

# Variables that control the position & font of the text.
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

# Inherits from the turtle class.


class Scoreboard(Turtle):

    # Controls the color, creation of the scoreboard.
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    # Creates & updates the scoreboard when food is collected or the game is reset.
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    # Checks to see of the score is greater than the high score and updates the text file
    # if true. It then resets the score.
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # Increases the score after every food is collected.
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
