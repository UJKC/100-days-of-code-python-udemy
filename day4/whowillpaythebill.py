import random

print("I will pay the bill. Thats what you should say.")
string = input("Enter all the names of people involved. Separated by comma and space ofcouse: ")
peopleinvolved = string.split(", ")
print(peopleinvolved)
i = len(peopleinvolved)
rand = random.randrange(0, i - 1)
print(f"This guy should pay the bill. And the person is: {peopleinvolved[rand]}")