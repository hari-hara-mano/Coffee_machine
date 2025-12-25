from turtle import Turtle,Screen

screen=Screen()

ALIGNMENT="center"
FONT = ("Arial", 18, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0, 260) 
        self.shape(None)  
        self.hideturtle()    
        self.update()
        

    def update(self):

        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)

    def game_over(self):

        self.color("yellow")
        self.goto(0,0)
        self.write(f" Game Over ", align=ALIGNMENT, font= FONT)
        screen.exitonclick()

    def increase(self):
        self.score+=1
        self.clear()
        self.update()


