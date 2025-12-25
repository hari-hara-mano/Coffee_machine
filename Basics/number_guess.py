import random

print(" Welcome to number guessing game ")
x=int(input("Enter range u want to guess :"))



y=random.randint(1,x)
print(y)


def play(lives):
    
    while lives>0:

        try:
            guess=int(input(f"You have {lives} left, make a guess : "))
            

        except ValueError:
            print("  Idiot only integers  ")
            continue
        
        if guess==y:
                print(f" Good guess {y} ")
                return
        elif guess > y:
                print(f" High guess a bit low ")
        else:
                print(f" LOW guess a bit high ")
        lives-=1


    print(f" Out of Lives, Game over, number was {y}")    
       





difficulty = input(" Enter your difficulty E for easy and D for difficult : ").lower().strip()

if difficulty=="e":
        play(10)
elif difficulty=="d":
        play(5)
else:
        print(" Only E or D idiot")


