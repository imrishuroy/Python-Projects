import requests
from datetime import datetime

USERNAME = "imrishuroy"
TOKEN = "theloveforairtelwillneverend"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# creating new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hr",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# creating coding graph

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

# Posting today's data to the graph

# today = datetime(year=2021, month=7, day=3)
today = datetime.now()
print(today.strftime("%Y%m%d"))
formatted_date = today.strftime("%Y%m%d")
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "14.5",


}


today_graph_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(today_graph_response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

pixel_data = {
    "quantity": "12.5"
}

# update data by put method

pixel_update_response = requests.put(url=update_pixel_endpoint, json=pixel_data, headers=headers)
print(pixel_update_response.text)

# delete data by put method

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
#
# delete_response = requests.delete(delete_pixel_endpoint, headers=headers)
# print(delete_response.text)
