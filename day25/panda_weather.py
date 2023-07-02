import pandas

count = 0

data = pandas.read_csv("day25\weather_data.csv")
print(data)
print("Days")
print(data['day'])
print("Temperature")
print(data['temp'])
print("Condition")
print(data['condition'])
data_list = data["temp"].to_list()
MAX_TEMP = max(data_list)
print(f"Max Temperature: {max(data_list)}")
length = len(data_list)
print(f"Total data: {len(data_list)}")
print(data.describe())
print(data.to_dict())
data_dic = data.to_dict()
print(f"Day and Condition on max Temperature: {data[data['temp'] == MAX_TEMP]}")
day = data[data['temp'] == MAX_TEMP]
print("Condition on max Temperature: "+ day["condition"])