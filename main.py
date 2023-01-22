import time
from scorebord import Score
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # finding the snake hit the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increaseScore()

    # Deduct the wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.gameOver()

    # Deduct body collision
    for segment in snake.new_turtle[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.gameOver()
screen.exitonclick()
