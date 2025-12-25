from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title(" Mana Kosam ra Chinnu ")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

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

    #Collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        score.increase()
        snake.extend()

    #Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #Collison with tail
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_is_on = False
            score.game_over()




