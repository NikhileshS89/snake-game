from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

def play_game():
    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
            game_is_on = False
            score.game_over()

        # Detect collision with snake body
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 1:
                game_is_on = False
                score.game_over()

    play_again = screen.textinput("Game Over", "Do you want to play again? (yes/no)").lower()
    if play_again == "yes":
        screen.clear()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Snake Xenzia")
        screen.tracer(0)
        play_game()
    else:
        screen.bye()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

play_game()
