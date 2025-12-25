from turtle import Turtle, Screen
import random

def random_rgb():
    return (random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255))

screen = Screen()
screen.colormode(255)

chinnu = Turtle()
chinnu.speed(0)

chinnu.width(1)
def spirograph(radius, gap):
    for _ in range(int(360 / gap)):
        chinnu.color(random_rgb())
        chinnu.circle(radius)
        chinnu.setheading(chinnu.heading() + gap)

    chinnu.home()        
    chinnu.setheading(0)

spirograph(radius=112, gap=3)

screen.exitonclick()
