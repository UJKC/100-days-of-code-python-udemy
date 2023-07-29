import requests

Sheety_endpoint = "https://api.sheety.co/22d264e8ad79207275125e9853aeb27f/copyOfFlightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        self.response_destination_data = requests.get(url=Sheety_endpoint)
        return self.response_destination_data
    
    # {'prices': [{'city': 'Paris', 'iataCode': 'CDG', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'SXF', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'HND', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'MCY', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'JFK', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'NLP', 'lowestPrice': 378, 'id': 10}, 
    # {'city': 'Bombay', 'iataCode': 'BOM', 'lowestPrice': 400, 'id': 11}]}