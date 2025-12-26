from turtle import Turtle,Screen

screen=Screen()

ALIGNMENT="center"
FONT = ("Arial", 18, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 260) 
        self.shape(None)    
        self.hideturtle()    
        self.update()
        

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font= FONT)

    def g_reset(self):
        if self.high_score <  self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score=0
        self.update()


    def increase(self):
        self.score+=1
        self.update()


