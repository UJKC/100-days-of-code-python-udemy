print("This gives average height of the boys in classroom.")
student_height = [180, 124, 165, 173, 189, 169, 146]
num = len(student_height)
average = 0
for height in student_height:
    average += height
total_average = average / num
print(f"Average height is: {total_average}")