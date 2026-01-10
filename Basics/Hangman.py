import random

stages=["ANIMATION 0","ANIMATION 1","ANIMATION 2","ANIMATION 3","ANIMATION 4","ANIMATION 5","ANIMATION 6","ANIMATION 7"]

word_list=["baboon","camel","aardvark","manor","Chinna","harishtha"]
chosen_word=random.choice(word_list)
print(chosen_word)

place_holder=""
for i in chosen_word: 
    place_holder+=" _ "
print(place_holder)

lives=7
temp=""

while 0<=lives<8:
    if lives==0:
        print("You lose")
        break


    guess= input("Guess a letter : ").lower()

    if guess in chosen_word:
        print(f"Correct guess {guess}, Lives left:{lives}")
        if guess in temp:
            print("Already Entered")
        print(stages[lives])
    else :
        lives-=1
        print(f"Wrong guess :{guess}, Lives left{lives}")
        print(stages[lives])
    

    display=""
    for i in chosen_word:
        if i==guess:
            display+=i
            temp+=i
            
        elif i in temp:
            display+=i

        else:
            display+=" _ "
           
            

    print(display)
    

    if "_" not in display:
        print("Game over, You win")
        break




