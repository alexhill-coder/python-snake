# Uses the turtle module to set up the screen.
from turtle import Screen

# Imports other files to control the characteristics of the snake, spawn food
# and control the scoreboard.
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#  Uses the time datatime module to control the refresh rate of the screen.
import time

# Sets the screen size, background color, title and stops automatic screen updates.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Calls functions from the other files.
snake = Snake()
food = Food()
score = Scoreboard()

# Sets up the controls to control the snake's direction.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Puts the game in a loop that restarts on losing.
game_is_on = True
while game_is_on:
    # Updates every loop.
    screen.update()
    time.sleep(0.1)
    snake.move()

#    Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

#   Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

#   Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()




