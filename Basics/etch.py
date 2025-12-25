from turtle import Turtle, Screen
import random

screen=Screen()
colour=["brown3","darkolivegreen3","yellow","aquamarine2","deepskyblue","cyan2"]
codes = ["b", "g", "y", "a", "s", "c","q"]


screen.setup(width=600,height=600)

def create(a,c):
    chinnu=Turtle("turtle")
    chinnu.color(c)
    chinnu.speed(0)
    chinnu.penup()
    chinnu.goto(x=-250,y=a)
    return chinnu


#def race():
    while True:
        players[0].fd(random.randint(1,10))
        if players[0].xcor() >= 250:
            return "b"

        players[1].fd(random.randint(1,10))
        if players[1].xcor() >= 250:
            return "g"
            
        players[2].fd(random.randint(1,10))
        if players[2].xcor() >= 250:
            return "y"
        
        players[3].fd(random.randint(1,10))
        if players[3].xcor() >= 250:
            return "a"
        
        players[4].fd(random.randint(1,10))
        if players[4].xcor() >= 250:
            return "s"
            
        players[5].fd(random.randint(1,10))
        if players[5].xcor() >= 250:
            return "c"
        
def race():
    while True:
        for idx, turtle in enumerate(players):
            turtle.forward(random.randint(1, 10))
            if turtle.xcor() >= 250:
                return codes[idx]



b=-220
players=[]
for i in colour:
    players.append(create(b,i))
    b+=75

bet=screen.textinput("Bet on?", "b for Brown, green, yellow, aquamarine, skyblue, cyan( Q to quit) ").lower().strip()

if bet in codes:

    msg=race()
    if bet==msg:
        print( f"You won {msg} is winner")
    else:
        print(f"you lost {msg} is winner ")

else:
    print(f" wrong input {bet}")
    

screen.exitonclick()