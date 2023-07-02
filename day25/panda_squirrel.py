import pandas

data = pandas.read_csv("day25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data)
print("Gray Fur Color")
data_gray  = data[data["Primary Fur Color"] == "Gray"]
print(data_gray)
print(f"NO of birds with Gray Fur are: {len(data_gray)}")
Gray_count = len(data_gray)
print("Black Fur Color")
data_black  = data[data["Primary Fur Color"] == "Black"]
print(data_black)
print(f"NO of birds with Gray Fur are: {len(data_black)}")
Black_Count = len(data_black)
print("Cinnamon Fur Color")
data_Cinnamon  = data[data["Primary Fur Color"] == "Cinnamon"]
print(data_Cinnamon)
print(f"NO of birds with Gray Fur are: {len(data_Cinnamon)}")
Cinnamon_Count = len(data_Cinnamon)
print("Dictionary data")
dictionary = {
    "Fur": ["Gray", "Black", "Cinnamon"],
    "Count": [Gray_count, Black_Count, Cinnamon_Count]
}
data_dick = pandas.DataFrame(dictionary)
print(data_dick)
data_dick.to_csv("day25\\output.csv")