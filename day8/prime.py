print("Prime Number Checker")
number = int(input("Enter the number to be checked: "))
flag = True
if number == 1:
    print("Composite number")
if number <= 0:
    print("Try another number")
for i in range(2, number):
    if number % i == 0:
        flag = False
if flag:
    print("Prime number")
else:
    print("Composite Number")