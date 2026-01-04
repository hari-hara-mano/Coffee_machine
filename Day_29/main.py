from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = ([(random.choice(letters)) for char in range(nr_letters)] 
    + [(random.choice(symbols)) for char in range(nr_symbols)] 
    + [(random.choice(numbers)) for char in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    generate_password_button.config(state="disabled")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_input.get().title()
    mail = email_input.get()
    password = password_input.get()
    pyperclip.copy(password)

    new_data = {
         website : {
              "email" : mail,  
              "password" : password

         }
    }


    if len(website) > 0 and len(mail) > 0 and len(password) > 0:

        def part():
            with open("data.json", mode="r") as data:
                #read existing data from data.json
                data_update = json.load(data)
                #update with new data
                data_update.update(new_data)

            with open("data.json", mode= "w") as data:
                #save the updated data
                json.dump(data_update, data, indent=4)

          
        messagebox.showinfo(title="Saved", message= f"Saved details \n website: {website} \n Email: {mail} \n Password :{password} ")
        try:
            part()
        
        except FileNotFoundError:

            with open("data.json", mode= "w") as data:
                #save the updated data
                json.dump(new_data, data, indent= 4)
            

            website_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo(title="Saved", message="Password saved successfully")
            generate_password_button.config(state="normal")
            
                    
    else:
        messagebox.showinfo(title="Not Saved", message="Re- Enter details")

# ---------------------------- FIND PASWORD ------------------------------- #     
def find_password():

    try:
        with open("data.json", "r") as data:
            data_file = json.load(data)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data found")
        
    else:
        user_input = website_input.get().title()
        if user_input in  data_file:
            email = data_file[user_input]["email"]
            password = data_file[user_input]["password"]
            messagebox.showinfo(title=f"{website_input}", message=f"Email: {email} \nPassword: {password}")

        else:
            messagebox.showinfo(title="No data", message=f"{user_input} not found")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

canvas = Canvas(height=200, width=200)
logo_png = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_png)
canvas.grid(row= 0, column= 1)

website_label = Label(text="Website", font=("Arial", 10, "bold"))
website_label.grid(row= 1, column= 0, sticky="w")

password_label = Label(text="Password", font=("Arial", 10, "bold"))
password_label.grid(row= 3, column= 0, sticky= "w")

email_label = Label(text="Email/Username", font=("Arial", 10, "bold"))
email_label.grid(row= 2, column= 0, sticky="w")

website_input = Entry()
website_input.grid(row= 1, column= 1, sticky="ew")
website_input.focus()

email_input = Entry()
email_input.grid(row= 2, column= 1, columnspan= 2, sticky="ew")
email_input.insert(0, "manoharchinnu@gmail.com")

password_input = Entry()
password_input.grid(row= 3, column= 1, sticky="ew")

generate_password_button = Button(text= "Generate password", command= password_generator)
generate_password_button.grid(row= 3, column= 2)

add_button = Button(text= "Add", command= save_password)
add_button.grid(row= 4, column= 1, columnspan=2, sticky="ew")

search_button = Button(text= "Search", command= find_password)
search_button.grid(row= 1, column= 2, sticky="ew")

























window.mainloop()