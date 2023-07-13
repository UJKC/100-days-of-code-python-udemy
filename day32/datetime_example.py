import datetime as dt

need = dt.datetime.now()
print(need)
year = need.year
print(year)
month = need.month
print(month)
day = need.day
print(day)
no_of_day = need.weekday()
print(no_of_day)
if year == 2020:
    print("Need face mask")
else:
    print("NO need")

date_of_birth = dt.datetime(year=2004, month=1, day=31)
print(date_of_birth)