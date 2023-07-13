import datetime as dt
import random
import smtplib

need = dt.datetime.now()
day_of_week = need.weekday()
if day_of_week == 0:
    with open("day32\\quotes.txt") as quotes:
        quotes_read = quotes.readlines()
    number_quotes = random.randint(0, len(quotes_read))
    random_quotes = quotes_read[number_quotes]

    my_email = "ujwalkcsps@gmail.com"
    password = ""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject:Monday Motivation\n\n{random_quotes}")