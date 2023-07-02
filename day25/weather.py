import csv

day = []
temperature = []
condition = []

with open("day25\weather_data.csv") as csv_file:
    formatter_file = csv.reader(csv_file)
    for rows in formatter_file:
        print(rows)
        if rows[1] != "temp":
            temperature.append(int(rows[1]))
            max_temp = max(temperature)
        if rows[0] != "day":
            day.append(rows[0])
        if rows[2] != "condition":
            condition.append(rows[2]) 
    print("Temperatures")
    print(temperature)
    print("Day")
    print(day)
    print("Condition")
    print(condition)
    print("Max Temperature")
    print(max_temp)
    