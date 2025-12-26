import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard




screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
manager=CarManager()
manager.hideturtle()
score=Scoreboard()

screen.onkey(player.up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.create_car()
    manager.move_car()
    
    #Detect collision with car
    for i in manager.all_cars:
        if player.distance(i) < 20 :
            
            game_is_on =False
   
    #Detect turtle crossed the path
    if player.is_at_finish_line():
        player.go_to_start()
        manager.increase_speed()
        score.level_up()




screen.exitonclick()