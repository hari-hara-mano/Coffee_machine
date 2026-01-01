def add(*args):
    a = 0
    for i in args:
        a=a+i
    return a

nums= input("enter values :").split()
nums=[int(i) for i in nums]
ans= add(*nums)
print(ans)