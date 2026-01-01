from tkinter import *

def button_click():

    i_text=input.get()
    my_chinnu.config(text=i_text)
    print("Thnaks for clicking")


window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=250)
window.config(padx=0, pady=0)

my_chinnu = Label(text="My Everything", font=("arial", 18, "bold"))
my_chinnu.config(text="Bujji")
my_chinnu.config(text="is equal to")
my_chinnu.place(x=125, y=200)

miles_label=Label(text="Miles", font=("arial", 10, "bold"))
miles_label.grid(row=2, column=6)

km_label=Label(text="Km", font=("arial", 10, "bold"))
km_label.grid(row=6, column=6)

button=Button(text="caluclate", command=button_click)
button.grid(row=20, column=4)


input=Entry()
print(input.get())
input.grid(row=2, column=4)


 
















window.mainloop()