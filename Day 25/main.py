import turtle
import pandas

screen=turtle.Screen()
chinnu=turtle.Turtle()
chinnu.hideturtle()
chinnu.penup()
screen.title(" U.S New Game ")
path= "blank_states_img.gif"
screen.addshape(path)
turtle.shape(path)




    


#def get_mouse_coor(x,y):
#    print(x,y)

#turtle.onscreenclick(get_mouse_coor)

data = pandas.read_csv("50_states.csv")
states= data.state.to_list()

correct_ans=[]

while len(correct_ans) < 50:

    ans = (screen.textinput(title= f"Score: {len(correct_ans)}/50 ", prompt=" Next state name ")).title()

    
    if ans == "Exit":

        un_answerd= [i for i in states if i not in correct_ans]

        df = pandas.DataFrame(un_answerd, columns= ["States"])
        df.to_csv("Missed_states.csv", index = False)
        break
    
    if ans in states and ans not in correct_ans:

        correct_ans.append(ans)

        row = data[data.state == ans]        
        x =int(row.x.item())
        y =int(row.y.values[0])

        chinnu.goto(x,y)
        chinnu.write(ans, align="center",font=("ariel", 12, "bold"))
    





turtle.mainloop()



