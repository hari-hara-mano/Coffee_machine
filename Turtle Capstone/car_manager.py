from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        x=random.randint(1,10)
        if x==1:
            car=Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(280,random.randint(-200,200))
            car.setheading(180)
            self.all_cars.append(car)

    def move_car(self):
        for i in self.all_cars:
            i.fd(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
