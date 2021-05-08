import requests
api_key = "b5a591867ecaf84b555a15b6ed6f92c2"

# parameters ={
#     "q":"Patna",
#     "appid": "b5a591867ecaf84b555a15b6ed6f92c2"
# }
#
# response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parameters)
# data = response.json()
# print(data)

parameters ={
    "appid": "b5a591867ecaf84b555a15b6ed6f92c2",
    "lat": 25.612677,
    "lon": 85.158875,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall" , params=parameters)
data = response.json()
print(data)
