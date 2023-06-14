print("No of days in that particular month in particular year")
days1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Month 2 has 29 days")
            else:
                print("Month 2 has 28 days")
    else:
        print("Month 2 has 28 days")
def days(month, year):
    if month == 2:
        leap(year)
    else:
        if month > 0:
            months = month - 1
            day = days1[months]
            print(f"Month {month} has {day} days")
month = int(input("Enter the month: "))
year = int(input("Enter the year to be considered: "))
days(month, year)