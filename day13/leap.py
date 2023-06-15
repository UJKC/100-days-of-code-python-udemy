#Question:

#print("Leap year calculator")
#year = int(input("Enter the input year: "))
#if year % 4 == 0:
#    if year % 100 == 0:
#    if year % 400 == 0:
#            print("Year is Leap year")
#        else:
#            print("Year is not leap year")
#else:
#    print("Year is not leap year")

#Answer:

print("Leap year calculator")
year = int(input("Enter the input year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Year is Leap year")
        else:
            print("Year is not leap year")
    else:
        print("Year is leap year")
else:
    print("Year is not leap year")