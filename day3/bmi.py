print("This will show your body mass index")
print("bmi is body weight(in kg) * height^2(in m)")
weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))
print("Your bmi is: "+ str(weight/(height ** 2)))