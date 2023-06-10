print("This calculates the days, weeks, months, years to live for 90 days, 70 days. Good luck.")
age = int(input("Enter your age: "))
remaining_age = 90 - age
remaining_weeks = remaining_age * 52
remaining_months = remaining_age * 12
remaining_days = remaining_age * 365
print(f"Your remaining life is: {remaining_age} years, {remaining_weeks} weeks. {remaining_months} months, {remaining_days} days")
print("For average life expectance: ")
remaining_age1 = 70 - age
remaining_weeks1 = remaining_age * 52
remaining_months1 = remaining_age * 12
remaining_days1 = remaining_age * 365
print(f"Your remaining life is: {remaining_age1} years, {remaining_weeks1} weeks. {remaining_months1} months, {remaining_days1} days")