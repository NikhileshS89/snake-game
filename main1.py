from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0) 

snake = Snake()
#When we call/create this object , we're calling 
# __init__(self) and then this intur calling
# create.snake() 
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

    #Detect collision method
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299 :
    # if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        score.game_over()

    #Detect head collided with any snake segment
    for segment in snake.segments[1:] :
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()