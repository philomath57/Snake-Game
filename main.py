from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.snake_body[0].xcor() > 300 or snake.snake_body[0].xcor() < -300 or snake.snake_body[0].ycor() > 300 or snake.snake_body[0].ycor() < -300:
        game_on = False
        scoreboard.game_over()

    for body_part in snake.snake_body:
        if body_part == snake.snake_body[0]:
            pass
        elif snake.snake_body[0].distance(body_part) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()