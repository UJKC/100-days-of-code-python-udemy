print("Welcome to fake pizza shop!")
print("What can i get for you?")
pizza_size = int(input("1. Small\n2. Medium\n3. Large\nEnter your options by number: "))
billamount = 0
if pizza_size == 1:
    billamount += 15
    pepperoni = int(input("Do you want extra pepperoni?\n1. Yes\n2. No\nYour Choice: "))
    if pepperoni == 1:
        billamount += 2
elif pizza_size == 2:
    billamount += 20
    pepperoni1 = int(input("Do you want extra pepperoni?\n1. Yes\n2. No\nYour Choice: "))
    if pepperoni1 == 1:
        billamount += 3
else:
    billamount += 25
    pepperoni2 = int(input("Do you want extra pepperoni?\n1. Yes\n2. No\nYour Choice: "))
    if pepperoni2 == 1:
        billamount += 3
cheese = int(input("Do you eant extra cheese?\n1. Yes\n2. No\nYour choice: "))
if cheese == 1:
    billamount += 1
print(f"Your total bill amount: {billamount}")