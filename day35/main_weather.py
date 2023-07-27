appid1 = ""
url1 =""

import requests


lat = 12.880394
lon = 77.554885

parameter = {
    'lat': lat,
    'lon': lon,
    'appid': appid1
}

response = requests.get(url=url1, params=parameter)
response.raise_for_status()
data = response.json()

if data['weather'][0]['id'] < 700:
    print("Please bring Umbrella")
else:
    print("No need")