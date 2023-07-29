import requests
import datetime

url_user_endpoint = "https://pixe.la/v1/users"

parameter_post = {
    #curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
    "token": "ujwalkcspsgmailcom",
    "username": "ujwal",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#Add a user
response = requests.post(url=url_user_endpoint, json=parameter_post)
response.raise_for_status()
print(response.status_code)
print(response.json())