while True :
    a = input("Select operation 1.Addition 2.Subtraction 3.Multiplication 4.Division :")

    try:
        a = int(a)
    except ValueError:
        print(f"Invalid Input {a}")
        continue

    if a not in (1,2,3,4):
        print(f"Chnage Input {a}")
    else:
        break
    
    
while True:
    x, y = input("Enter x,y: ").split(",")
    if x.isdigit() and y.isdigit():
        x=float(x)
        y=float(y)
        break
    else:
        print(f"Enter valid numbers not these u idiot {x},{y}")
        continue
    
if a==1:
        print(f"Addition of {x}&{y} is {x+y}")
elif a==2:
        print(f"Subtraction of {x}&{y} is {x-y}")
elif a==3:
       print(f"Multiplication of {x}&{y} is {x*y}")
elif a==4:
       if y==0:
        print("Infinity")
       else:
        print(f"Division of {x}&{y} is {x/y}")


