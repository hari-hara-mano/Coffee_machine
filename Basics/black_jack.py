import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print("Wanna play Black jack game Y or N..? ")
x=random.sample(cards,k=2)
score=sum(x)
print(f"Your Cards : {x}, Current score :{score}")  

c_cards=random.sample(cards,k=2)
c_score=sum(c_cards)
print(f"Computers 1st Card {c_cards[0]}")


while score<=21:

    i=input(f"Type Y to draw a card or N to submit your score {score}  : ").lower()
    if i=="y":
        c=random.choice(cards)
        print(f"Drawn card {c} ")
        score+=c
        x.append(c)
        if score >21:
            print(f"Game over total Score {score}")
            break
    else:
         print(f" Final score {x}, {score}")
         break

c_score=sum(c_cards)
print(f"Computers score {c_cards}, {c_score}")

while c_score <=21:
        
        if c_score==21 or c_score==20 or c_score==19 or c_score==18:
             break
        
        c_card=random.choice(cards)
        print(f" Computer Drawn card {c_card} ")
        c_score+=c_card
        c_cards.append(c_card)
        if c_score >21:
            print(f"Game over computer FInal Score in hand {c_cards}, {c_score}")
            break
        else:
             print(f"Computer score after drawn {c_cards},{c_score}")
             continue
        
if score>21 and c_score>21 :
     print(f"Both busted {score}, {c_score} ")
elif score==c_score:
     print(f"Draw Match {score}, {c_score} ")
elif score >21:
     print(f"Computer won {score}, {c_score} ")
else:
     print(f"You won {score}, {c_score} ")
             