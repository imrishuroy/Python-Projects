import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()

car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(timmy.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision with car
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect Successful collision
    if timmy.is_at_finish_line():
        timmy.reset()
        score_board.increase_level()
        car_manager.level_up()


screen.exitonclick()





    #car.random_position()
