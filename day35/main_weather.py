appid1 = ""
url1 =""

import requests
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""

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
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Please bring umbrella",
                     from_='',
                     to=''
                 )
    print(message.status)

else:
    print("No need")
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Please don't bring umbrella",
                     from_='',
                     to=''
                 )
    print(message.status)
