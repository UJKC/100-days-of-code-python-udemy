print("Paint Area Coverage")
height = float(input("Enter the height of the wall: "))
width = float(input("Enter the width of the wall: "))
coverage = float(input("Enter the area per square meter a can of paint can cover: "))
needed = (height * width) / coverage
print(f"The paint can needed to cover the area is: {needed}")