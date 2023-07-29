import requests
import datetime

date_time = datetime.datetime.now()

APP_ID = "9fc32c43"
API_KEY = "cc1032cc3e9072a67adcbf3ab1796877"

nutritionix_excersice_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_project_endpoint = "https://api.sheety.co/22d264e8ad79207275125e9853aeb27f/copyOfMyWorkouts/workouts"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

input_request_query = input("Enter what you did today: ")
input_request_gender = input("Enter your gender (male or female): ")
input_request_weight = float(input("Enter your weight: "))
input_request_height = float(input("Enter your height: "))
input_request_age = int(input("Enter your age: "))

parameter_post = {
    "query": input_request_query,
    "gender": input_request_gender,
    "weight_kg": input_request_weight,
    "height_cm": input_request_height,
    "age": input_request_age,
}

response_excersise = requests.post(url=nutritionix_excersice_endpoint, headers=header, json=parameter_post)
response_excersise.raise_for_status()
print(requests.status_codes)
data = response_excersise.json()

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date_time.strftime("%d/%m/%Y"),
            "time": date_time.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

response_sheets = requests.post(url=sheety_project_endpoint, json=sheet_inputs)
response_sheets.raise_for_status()

#import os
#os.environ["APP_ID"] = APP_ID
#APP_ID = os.environ["APP_ID"] – raises exception if key does not exist
#APP_ID = os.environ.get("APP_ID") – returns None if key does not exist
#APP_ID = os.environ.get("APP_ID", “Message”) – returns “Message” if key does not exist