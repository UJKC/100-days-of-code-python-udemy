##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




import pandas
import datetime as dt
import smtplib
import random

PLACE_HOLDER = "[NAME]"

with open("day32\\birthdays.csv")as birth:
    data = pandas.read_csv(birth)

need = dt.datetime.now()
for (index, row) in data.iterrows():
    if (row['year'] == need.year) and (row['month'] == need.month) and (row['day'] == need.day):

        random_letter = random.randint(1, 3)
        if random_letter == 1:
            with open("day32\\letter_templates\\letter_1.txt") as bd:
                happy = bd.read()
        elif random_letter == 2:
            with open("day32\\letter_templates\\letter_2.txt") as bd:
                happy = bd.read()
        else:
            with open("day32\\letter_templates\\letter_3.txt") as bd:
                happy = bd.read()
        hbd = happy.replace(PLACE_HOLDER, row["name"])


        my_email = "ujwalkcsps@gmail.com"
        password = ""
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject:Birthday Wishes\n\n{hbd}")