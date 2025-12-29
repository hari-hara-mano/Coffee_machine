import pandas

data=pandas.read_csv("C:/Users/windows/Downloads/Squirrel.csv")

gray=len(data[data["Primary Fur Color"] == "Gray"])
cinn=len(data[data["Primary Fur Color"] == "Cinnamon"])
black=len(data[data["Primary Fur Color"] == "Black"])

summary= pandas.DataFrame({"Colour" : ["Cinnamon", "Grey", "Black"],
                           "Count": [cinn,gray,black] })

summary.to_csv("data1.csv")

print(summary)



























#color=(data["Primary Fur Color"])
#c=0
#g=0
#b=0
#e=0
#for i in color:
#    if i == "Cinnamon":
#        c+=1
#    elif i == "Gray":
#        g+=1
#    elif i == "Black":
#        b+=1
#    else:
#        e+=1
#
#print(f"Cinnamon{c}, Grey:{g}, Black & extra:{b},{e}")
#
#summary= pandas.DataFrame({"Colour" : ["Cinnamon", "Grey", "Black", "Extra"],
#                           "Count": [c, g, b, e] })
#
#summary.to_csv("data.csv")
#
#print(summary)



