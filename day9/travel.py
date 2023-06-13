travel_log = [
    {
        "country" : "France",
        "visited" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visited" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    }
]
def addnewcountry(country, visited, cities):
    newcounter = [
        {
            "country" : country,
            "visited" : visited,
            "cities" : cities
        }
    ]
    travel_log.append(newcounter)
addnewcountry("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)