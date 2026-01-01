from tkinter import *

def button_click():

    input_text= round(float(miles_input.get())*1.609, 2)
    km_result_label.config(text= f"{input_text}")


window=Tk()
window.title("Miles to Km convertor")
window.config(padx=20, pady=20)

miles_input= Entry()
miles_input.grid(row=0, column=2)

miles_label =Label(text= "Miles")
miles_label.grid(row=0, column=3)

is_equal_label= Label(text="is equal to")
is_equal_label.grid(row=1, column=1)

km_result_label = Label(text= "0")
km_result_label.grid(row=1, column=2)

km_label= Label(text= "Km")
km_label.grid(row=1, column=3)

caluclate_button= Button(text="Calucalte", command= button_click)
caluclate_button.grid(row=2, column=2)














window.mainloop()