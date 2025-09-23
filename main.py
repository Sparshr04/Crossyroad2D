import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

iota = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=iota.move_up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collusion with the cars
    for car in car_manager.all_cars:
        if car.distance(iota) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect a successful crossing
    if iota.is_at_finish_line():
        iota.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick(