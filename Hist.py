import turtle as manu
from turtle import Screen
import random as rand




color_list=[ (250, 228, 16), (212, 13, 9), (199, 12, 36), (230, 228, 6), (196, 70, 20), (32, 90, 188), (235, 148, 38), (43, 212, 70), (33, 30, 152), (16, 22, 54), (67, 9, 48), (244, 39, 150), (14, 206, 223), (238, 244, 249), (66, 202, 229), (62, 21, 10), (225, 19, 111), (15, 155, 21), (228, 166, 9), (248, 11, 9), (245, 58, 16), (98, 75, 9), (223, 140, 203), (68, 240, 160), (10, 97, 62), (6, 39, 33), (68, 219, 157), (238, 157, 211), (91, 77, 205), (88, 225, 234), (250, 8, 12), (242, 166, 157), (178, 181, 224), (35, 242, 166), (9, 80, 112), (11, 59, 246)]

chinnu=manu.Turtle()
screen=Screen()
ran=rand.Random()
chinnu.speed(4004)
chinnu.setheading(210)
chinnu.penup()
chinnu.fd(600)
chinnu.setheading(180)
chinnu.fd(120)
chinnu.setheading(0)
chinnu.pendown()

chinnu.shape("turtle")
screen.colormode(255)
x=1
while x<23:
    for i in range(43):
        chinnu.dot(15, ran.choice(color_list))
        chinnu.penup()
        chinnu.fd(30)
        chinnu.pendown()

    chinnu.penup()
    chinnu.setheading(90)
    chinnu.fd(30)
    chinnu.setheading(180)
    chinnu.fd(1290)
    chinnu.setheading(0)
    chinnu.pendown()
    x+=1


screen.exitonclick()