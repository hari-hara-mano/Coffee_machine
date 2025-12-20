def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0: 
        raise ZeroDivisionError("Cannot divide by zero")
    
    return x/y

operation={}
operation["+"]=add
operation["-"]=sub
operation["*"]=mul
operation["/"]=div



def caluclator():

    a=float(input("Enter 1st num :"))
    while True:

        try:

            o=input("Enter Operation to perform\n +\n -\n * \n / ").strip()
            b=float(input("Enter 2nd num : "))

            z=operation[o](a,b)
        

            if o=="+":
                
                print(f"Addition : {z}")
            if o=="-":
                
                print(f"sub : {z}")
            if o=="*":
                
                print(f"multiplition : {z}")
            if o=="/":
                
                print(f"division : {z}")
            
            i=input(f"wanna continue with result {z} type y for yes n for No or want new caluclation prees e :").strip().lower()
            if i=="y":
                a=z
                continue
            elif i=="e":
                caluclator()
            elif i=="n":
                print("End of clauclation")
            else:
                print("wrong input x ")
                

        except ValueError:
            print("wrong input")
            break
        except ZeroDivisionError as e:
            print(e)
            a = float(input("Enter 1st num again to continue: ")) 
        except KeyError:
            print("try again with cooreect inputs kojja")
    
caluclator()
   
































































"""a=float(input("Enter 1st num : "))

while True:

    try:

        
        b=input("Enter operation : \n+ \n- \n* \n/ ")

        if b not in ["+", "-", "*", "/"]:
            raise ValueError
        if b=="+":
            print(z:=add(a,float(input("Enter second number : "))))
        if b=="-":
            print(z:=sub(a,float(input("Enter second number : "))))
        if b=="*":
            print(z:=mul(a,float(input("Enter second number : "))))
        if b=="/":
            print(z:=div(a,float(input("Enter second number : "))))
        
        i=input(f" Do u want to contine with result :{z} press y for yes N for No :").lower().strip()
        if i=="y":
            a=z
        else:
            print("U r done...!")
            break

    except ValueError:
        print("wrong input")
        break
    except ZeroDivisionError as e:
        print(e)
        a = float(input("Enter 1st num to continue: "))"""