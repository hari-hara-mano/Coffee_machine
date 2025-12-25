alpha= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caser(direction,original_text,shift_amount):
   

   if direction=="f":
        y=""
        for i in original_text:
        
            if i in alpha:
                x= alpha.index(i)
                if x+shift_amount>=len(alpha):
                   x=(x+shift_amount)%len(alpha)
                   y=y+alpha[x]
                else:
                   x+=shift_amount
                   y=y+alpha[x]     
        print(y)


   if direction=="b":
        y=""
        for i in original_text:
        
            if i in alpha:
                x= alpha.index(i)
                if x-shift_amount<0:
                    x=((x-shift_amount)%len(alpha))
                    y=y+alpha[x]
                else:
                    x-=shift_amount
                    y=y+alpha[x]
        print(y)
    
    
caser(direction=input(" Enter which way text to be encoded f for forward or b for backward").lower(),original_text=input("Enter text to be converted :"),shift_amount=int(input("Shifted to :")))
   