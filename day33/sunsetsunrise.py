import requests

MY_LAT = 12.880245
MY_LONG = 77.554871

position = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=position)
response.raise_for_status()

data = response.json()
print(data)

sunrise = data['results']['sunrise']
print(sunrise)
sunset = data['results']['sunset']
print(sunset)
data_Split_sunrise = sunrise.split("T")[1].split(":")[0]
print(data_Split_sunrise)
data_Split_sunset = sunset.split("T")[1].split(":")[0]
print(data_Split_sunset)