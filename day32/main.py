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
    if (row['month'] == need.month) and (row['day'] == need.day):

        random_letter = random.randint(1, 3)
        with open(f"day32\\letter_templates\\letter_{random_letter}.txt") as bd:
            happy = bd.read()
        hbd = happy.replace(PLACE_HOLDER, row["name"])


        my_email = "ujwalkcsps@gmail.com"
        password = ""
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row["email"], msg=f"Subject:Birthday Wishes\n\n{hbd}")