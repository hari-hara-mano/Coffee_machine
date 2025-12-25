from menu import Menu 
from coffee_maker import CoffeeMaker 
from money_machine import MoneyMachine 

n=MoneyMachine()
c=CoffeeMaker()
m=Menu()



while True:

    s=m.get_items()
    print(s)
    choice=input(f"What would you like? {s} :").lower().strip()
    if choice=="off":
        break
    elif choice=="report":
        n.report()
        c.report()
    else:
        drink=m.find_drink(choice)
        msg=c.is_resource_sufficient(drink)
        if msg:
            if n.make_payment(drink.cost):
                c.make_coffee(drink)

    

