#import smtplib
#
#
#
#my_email = "kp9888203@gmail.com"
#
#with smtplib.SMTP("smtp.gmail.com") as connection :
#    connection.starttls()
#    connection.login(user="kp9888203@gmail.com", password="svlt rgfj yjbk tmhi")
#    connection.sendmail(
#        from_addr= my_email,
#                        to_addrs="harikakalamati333@gmail.com", 
#                        msg="Subject: Hey ra Kanna\n\n love you 3000, Miss you badly 5000, kiss you 10000, " \
#                        "hug you 15000, wanna be yours : Infinite\n\n " \
#                        "bujji this is a test mail sent via programm naku 1st attempt idi sending lo tappulem " \
#                        "lekpaothe direct vachestadi..my buchki buchki dinosaur," \
#                        " emojis veltayo ledo lots of love emojis..:)"
#                        )
#    connection.close()

























import random
import datetime as dt
import smtplib

today = dt.datetime.now()

with open("quotes.txt") as data:
    quotes = data.readlines()

if today.weekday() == 1 and today.hour == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= "kp9888203@gmail.com", password= "svlt rgfj yjbk tmhi")
        connection.sendmail(from_addr= "kp9888203@gmail.com",
                             to_addrs= "lovelysaimanohar143@gmail.com",
                               msg= f"Subject : Motivation Monday \n\n {random.choice(quotes)}"
                               )
    print("done")


