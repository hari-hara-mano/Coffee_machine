from turtle import Turtle, Screen
import random

Screen().colormode(255)
chinnu=Turtle()
chinnu.shape("turtle")
def random_rgb():
    return (random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255))




dir=[0,90,180,270]
def execution(a):
          
          chinnu.color(random_rgb())
          
          for x in range(a):
            chinnu.forward(4)
            chinnu.right(2)   

chinnu.home()
chinnu.speed(24)
#i=int(input( " Enter Range "))

execution(500)    
 
        

Screen().exitonclick()




























