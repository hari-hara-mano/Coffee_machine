from turtle import Turtle

POSITIONS =[(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE=20
class Snake:

    def __init__(self):      
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for i in POSITIONS:
            chinnu=Turtle("square")
            chinnu.color("cyan2")
            chinnu.penup()
            chinnu.goto(i)
            self.segments.append(chinnu)

    def move(self):

        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)

        self.segments[0].fd(MOVE_DISTANCE)

    def Up(self):
        self.chinnu.heading(0)
        
