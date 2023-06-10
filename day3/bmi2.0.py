print("This will show your body mass index")
print("bmi is body weight(in kg) * height^2(in m)")
weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))
bmi = weight/(height ** 2)
print("Your bmi is: "+ str(bmi))
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinical obese")