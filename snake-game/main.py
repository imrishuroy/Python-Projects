from turtle import Screen

from scoreboard import ScoreBoard
import time
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

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
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset() 

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

    # Detect collision with tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score_board.game_over()







screen.exitonclick()

# timmy = Turtle(shape="square")
# timmy.color("white")
# print(timmy.xcor())
# print(timmy.ycor())
#
#
# tommy = Turtle(shape="square")
# tommy.color("white")
# tommy.goto(x=-20.0, y=0.0)

# x_cordinate = 0.0
#
# snake = []
#
# for turtle in range(3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.goto(x=x_cordinate, y=0.0)
#     x_cordinate -= 20
#     snake.append(new_turtle)
#
# print(snake)
