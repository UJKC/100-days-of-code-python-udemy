print("Welcome to tip calculator")
total_bill = float(input("Enter the total bill amount: "))
tip = float(input("Enter the total tip amount: "))
total_person = int(input("Enter number of people the bill has to split: "))
each = (total_bill * (1 + (tip / 100))) / total_person
print(f"Each person has to pay: {each}")