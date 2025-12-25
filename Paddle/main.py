from turtle import Screen
from c_paddle import Paddle
from ball import Ball
from score import Score
import time



screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(" Mana Kosam ra Chinnu ")
screen.listen()
screen.tracer(0)



r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()
score=Score()




screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True

while game_is_on:
    time.sleep(ball.b_speed)
    screen.update()
    ball.move()

# Detect right misses
    if ball.xcor() > 380 :
        ball.p_reset()
        score.l_point()

# Detect left misses
    if ball.xcor() < -380 : 
        ball.p_reset()
        score.r_point()

# Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

# Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
    





























screen.exitonclick()