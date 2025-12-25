details={}

def bid():
    a=0
    for i,j in details.items():
        if a<j:
            a=j
            winner = i
    print(f"Highest bid {winner}:{a}")       

while True:
    x=input(" Welocme to Bid game,\n Enter your name to continue: ")
    y=int(input("Enter Bid amount : "))
    z=input("Are there ny other bids..? y for yes N for no : ").lower()
    details[x]=y
    if z=="y":
        print("\n"*100)
        continue
    elif z=="n":
        break

bid(details)


print(details)

