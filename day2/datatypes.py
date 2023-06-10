print("Welcome to fake calculator")
print("Welcome: Type only 2 digit integers now")
number = int(input("Enter the number: "))
print("Your answer is: "+ str(int((number / 10)) + int(number % 10)))