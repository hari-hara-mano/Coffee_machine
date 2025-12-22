from turtle import Screen
from snake import Snake
import time
from food import Food

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title(" Mana Kosam ra Chinnu ")
screen.tracer(0)

snake=Snake()
food=Food()

screen.listen()

screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

game_is_on= True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <15:
        print("yup")

