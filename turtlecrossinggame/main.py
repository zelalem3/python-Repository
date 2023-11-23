import time
from player import Player
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_On = True
while game_is_On:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_On = False

    if player.is_at_finish_line():
        player.go_to_starting_line()
        car_manager.level_up()

screen.exitonclick()
