import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}
#x = student_dict.intems()
#for (key, value) in x:
#   print(key)
data = pandas.DataFrame(student_dict)
print(data)
x = data.items()
#panda iter
#for (key, value) in x:
#   print(key)
y = data.iterrows()
for (item, value) in y:
    print(item)
    print(value)
    print(value["student"])