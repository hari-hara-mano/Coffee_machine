##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas
import datetime as dt
import random
import smtplib


today= dt.datetime.now()      
today_tuple= (today.month, today.day)

b_data = pandas.read_csv("birthdays.csv")
birthday_dict = {(d_row.month, d_row.day) : d_row for (index, d_row) in b_data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        file = letter.read()
        file = file.replace("[NAME]", birthday_dict[today_tuple]["name"])
        file = file.replace("Angela", "Manu gadu")
        print(f"\n{file}")

# 4. Send the letter generated in step 3 to that person's email address.
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= "kp9888203@gmail.com", password= "svlt rgfj yjbk tmhi")
        connection.sendmail(from_addr= "kp9888203@gmail.com",
                             to_addrs= "lovelysaimanohar143@gmail.com",
                             msg= f"Subject : Dula teerchindi ra ee session \n\n {file}\nNti ra manu manki ee dula sarele" \
                             " ndku chestunnamo grttu undi kada antha mana kosam m,chinnu kosam, " \
                             "basic ga complaining manki antha acchi radu aradu be a man u can do it ra manu " \
                             "love you. "
                             )
        





