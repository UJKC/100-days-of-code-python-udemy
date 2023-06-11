print("Get the heighest score oin the class")
score = [76, 65, 89, 86, 55, 91, 64, 89]
highest = 0
for high in score:
    if highest < high:
        highest = high
print(f"Highest score in the class is: {highest}")