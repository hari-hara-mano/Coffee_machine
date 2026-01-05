from tkinter import *
from pandas import *
from random import *
from pandas.errors import *


BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn = {}

try:
    data= read_csv("data/unknown_words.csv")

except (FileNotFoundError, EmptyDataError):
    original_data = read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient= "records")

else:
    if data.empty:
        original_data = read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) 

    if not to_learn:
        canvas.itemconfig(card_title, text="Done 🎉", fill= "cyan")
        canvas.itemconfig(card_word, text="All words learned", fill= "cyan")
        return
    
    current_card = choice(to_learn) #random.choice
    canvas.itemconfig(canvas_image, image= card_front_img)
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= current_card["French"], fill= "black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image= card_back_img)
    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(card_word, text= current_card["English"], fill= "white")

def is_known():
    global current_card, to_learn
    to_learn.remove(current_card)
    unknown_words = DataFrame(to_learn)
    unknown_words.to_csv("data/unknown_words.csv", index= False)
    next_card()



window = Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width= 800, height= 526) 
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file= "images/card_back.png")    
canvas_image = canvas.create_image(400, 263, image= card_front_img)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
card_title = canvas.create_text(400, 150, text= "French", font= ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "word", font= ("Arial", 60, "bold"))
canvas.grid(row= 0, column= 0, columnspan= 2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image= cross_image, highlightthickness= 0, command= next_card)
unknown_button.grid(row= 1, column= 0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image= check_image, highlightthickness= 0, command= is_known)
known_button.grid(row= 1, column= 1)


next_card()


#window.grid_columnconfigure(1, weight=1)
#window.grid_columnconfigure(2, weight=1)



























window.mainloop()
