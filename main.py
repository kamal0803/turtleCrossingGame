# COMPLETED

from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

import time

screen = Screen()
screen.title("Turtle crossing game!")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
player.create_turtle()
car = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.go_up)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    car.create_car()
    car.move_cars()

    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.start_again()
        car.level_up()

    for c in car.all_cars:
        if player.player_turtle.distance(c) <= 20:
            player.player_turtle.write(arg="GAME OVER!", align='center', font=('New Times Roman', 20, 'normal'))
            game_is_on = False

screen.exitonclick()

