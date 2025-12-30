num= [1,2,3]
add_list= [n+1 for n in num]
print(add_list)

name= "chinnu"
manu = [i.upper() for i in name]
print(manu)

print([2*i for i in range(1,10)])

import random
import pandas

names= [
    "manu",
    "chinnu", 
    "kanna" ,
    "bujji" ,
    "love" ,
    "low" ,
    "avg"
]

stude_score={i : random.randint(30,100) for i in names}
print(stude_score)

passed_std = {i:j for i,j in stude_score.items() if j>35}
print(passed_std)

data = pandas.DataFrame(passed_std.items(), columns=["Name", "Score"])

print(data)

for index,row in data.iterrows():
   # print(index)
    print(row.Name)