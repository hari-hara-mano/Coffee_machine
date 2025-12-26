from turtle import Turtle

FONT = ("Arial", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level= 1
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.rite()

    def level_up(self):
        self.clear()
        self.level += 1
        self.rite()

    def rite(self):
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def g_over(self):
        self.home()
        self.write(f" GAME OVER ", align="center", font=FONT)
