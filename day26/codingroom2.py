weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
#weather_f = {newkey:value for (key, value) in dictionary.item()}
x = weather_c.items()
weather_f = {day:(temp_c * 9 / 5 + 32) for (day, temp_c) in x}
print(weather_f)