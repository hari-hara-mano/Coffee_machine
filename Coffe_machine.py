MENU = [{
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "cost": 1.5
        }
        }
        
    },

    {"cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "cost": 2.5
        }
        }
    }, 
    
    {"latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "cost": 3.0
        }
        }
    }
    
]


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
   
}

cash=0

def count(a):

    money=[]
    
    for i in ["quaters : ", "dimes : ", "nickles : ", "pennies : "]:
            while True:
                try:
                    money.append(float(input(i)))
                    break
                
                except ValueError:
                    print(f" False input, Try again ")


    amount = money[0]*0.25 + money[1]*0.10 + money[2]*0.05 + money[3]*0.01

    if a > amount:
        return False, " Not sufficient amount ", round(amount,3)
    elif a == amount:
        return True, " Thanks for exact change " , round(amount,3)
    else :
        return True, " Here's the change ", round(amount-a,3)






def make_coffe(a,b,c):

    global resources

    if a<=resources['water']:

        if b<=resources['milk']:

            if c<=resources['coffee']:
                resources['water']-=a
                resources['milk']-=b
                resources['coffee']-=c
                return "Here is your coffe"
            
            else:
                print(f" Not enough coffee {resources['coffee']} ")
                return
            
        else:
            print(f" Not enough milk {resources['milk']} ")
            return
        
    else:
        print(f" Not enough water {resources['water']} ")
        return


def coffe(user_choice):

    global cash
    global resources
    
    if user_choice=="e":
        print(f" Espresso costs {MENU[0]['espresso']['ingredients']['cost']}")
        status, msg , amount =count( MENU[0]['espresso']['ingredients']['cost'])
        print(msg,amount)
        if 'status'==True:
            cash+=MENU[0]['espresso']['ingredients']['cost']
            final_message=make_coffe(MENU[0]['espresso']['ingredients']['water'],0,MENU[0]['espresso']['ingredients']['coffee'])
            print(f" {final_message }")
            return " Espresso is my personal choice too.."
        else :
            return f" Sorry not suuficient amount {amount}"


    elif user_choice=="c":
        print(f"  costs {MENU[1]['cappuccino']['ingredients']['cost']}")
        status, msg , amount =count( MENU[1]['cappuccino']['ingredients']['cost'])
        print(msg,amount)
        if 'status'==True:
            cash+=MENU[1]['cappuccino']['ingredients']['cost']
            final_message=make_coffe(MENU[1]['cappuccino']['ingredients']['water'],MENU[1]['cappuccino']['ingredients']['milk'],MENU[1]['cappuccino']['ingredients']['coffee'])
            print(f" {final_message }")
            return " C in cappuchino represents cuteness in you "
        else :
            return f" Sorry not suuficient amount {amount}"
    

    elif user_choice=="l":
        print(f" Latte costs {MENU[2]['latte']['ingredients']['cost']}")
        status, msg , amount =count( MENU[2]['latte']['ingredients']['cost'])
        print(msg,amount)
        if 'status'==True:
            cash+=MENU[2]['latte']['ingredients']['cost']
            final_message=make_coffe(MENU[2]['latte']['ingredients']['water'],MENU[2]['latte']['ingredients']['milk'],MENU[2]['latte']['ingredients']['coffee'])
            print(f" {final_message }")
            return f" People can go for a war for Latte "
        else :
            return f" Sorry not suuficient amount {amount}"
    

    elif user_choice=="report":
        print(f" Report :\n Water :{resources['water']}, \n Milk :{resources['milk']}, \n Coffee :{resources['coffee']} ")
        return f"\n cash : {cash} "



need=True
while need:

    user_input=input("What would you like? \n E for espresso : \n L for latte : \n C cappuccino :").lower().strip()

    if user_input in ["e","l","c","report"]:
        msg=coffe(user_input)
        print(msg)

    elif user_input=="off":
        need = False

    else:
        print(f" Try that again your input {user_input} was wrong ")
        continue
    