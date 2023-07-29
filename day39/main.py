#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager as DM

sheety_requests = DM()
data_response_got_from_sheety = sheety_requests.get_destination_data()
print(data_response_got_from_sheety.json())