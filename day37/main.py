import requests
import datetime

url_user_endpoint = "https://pixe.la/v1/users"

parameter_post = {
    #curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

url_graph_endpoint = f"https://pixe.la/v1/users/{parameter_post['username']}/graphs"

parameter_graph = {
    #curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
    "id":"testgraph1",
    "name":"Reading",
    "unit":"commit",
    "type":"int",
    "color":"shibafu",
}

url_graph_endpoint_add = f"https://pixe.la/v1/users/{parameter_post['username']}/graphs/{parameter_graph['id']}"

headers = {
    "X-USER-TOKEN" : parameter_post["token"]
}

date_today = datetime.datetime.now()

parameter_add = {
    #curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
    "date": "",
    "quantity":"3"
}

#'X-USER-TOKEN:thisissecret'

#Add a user
#response = requests.post(url=url_user_endpoint, json=parameter_post)
#response.raise_for_status()
#print(response.status_code)
#print(response.json())

#Add a graph
#response = requests.post(url= url_graph_endpoint, json=parameter_graph, headers=headers)
#response.raise_for_status()
#print(response.status_code)
#print(response.json())

#Add a value on particular date
#response = requests.post(url= url_graph_endpoint_add, json=parameter_add, headers=headers)
#response.raise_for_status()
#print(response.status_code)
#print(response.json())