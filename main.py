import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

loop_count = 0
cars = []
ass = Player()
score = Scoreboard()
screen.listen()
screen.onkey(fun=ass.move_up, key='Up')

game_is_on = True
while game_is_on:
    loop_count += 1
    time.sleep(0.1)

    #Check whether the turtle has reached the finish line
    var = ass.finished_stage()
    if var:
        car.speed_increment()
        score.score()

    #Create cars at random
    if loop_count%2 ==0 and loop_count%3 ==0:
        car = CarManager()
        cars.append(car)

    #Move the car forward
    for car in cars:
        car.forward(car.move_increment*-1)
        #clear the list of cars when the car is out of vision
        if car.xcor()<-290:
            cars.remove(car)
            car.hideturtle()
        #detect colluison with turtle
        if car.distance(ass) < 20:
            game_is_on = False

        
    
    screen.update()
