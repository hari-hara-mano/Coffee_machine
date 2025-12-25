import turtle as manu
from turtle import Screen
import random as rand

color_list = [
    (250, 228, 16), (212, 13, 9), (199, 12, 36), (230, 228, 6),
    (196, 70, 20), (32, 90, 188), (235, 148, 38), (43, 212, 70),
    (33, 30, 152), (16, 22, 54), (67, 9, 48), (244, 39, 150),
    (14, 206, 223), (238, 244, 249), (66, 202, 229), (62, 21, 10),
    (225, 19, 111), (15, 155, 21), (228, 166, 9), (248, 11, 9),
    (245, 58, 16), (98, 75, 9), (223, 140, 203), (68, 240, 160),
    (10, 97, 62), (6, 39, 33), (68, 219, 157), (238, 157, 211),
    (91, 77, 205), (88, 225, 234), (250, 8, 12), (242, 166, 157),
    (178, 181, 224), (35, 242, 166), (9, 80, 112), (11, 59, 246)
]

screen = Screen()
screen.colormode(255)

chinnu = manu.Turtle()
chinnu.hideturtle()
chinnu.speed(0)
chinnu.penup()

DOT_SIZE = 15
GAP = 30
ROWS = 22
COLS = 43

start_x = -640
start_y = -300

for row in range(ROWS):
    chinnu.goto(start_x, start_y + row * GAP)
    for col in range(COLS):
        chinnu.dot(DOT_SIZE, rand.choice(color_list))
        chinnu.forward(GAP)

screen.exitonclick()
