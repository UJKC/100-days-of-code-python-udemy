#Question:

#print("FizzBuzz Game")
#for number in range(1, 100):
#    if number % 3 != 0 and number % 5 != 0:
#        print("FIZZ")
#    elif number % 5 == 0 and number % 3 == 0:
#        print("BUZZ")
#    else number % 3 == 0 or number % 5 == 0:
#        print("FIZZBUZZ")
#    else:
#        print(number)

#Answer:

print("FizzBuzz Game")
for number in range(1, 100):
    if number % 3 == 0 and number % 5 != 0:
        print("FIZZ")
    elif number % 5 == 0 and number % 3 != 0:
        print("BUZZ")
    elif number % 3 == 0 and number % 5 == 0:
        print("FIZZBUZZ")
    else:
        print(number)