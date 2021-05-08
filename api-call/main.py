import requests
from twilio.rest import Client

api_key = "b5a591867ecaf84b555a15b6ed6f92c2"
account_sid = "AC1beba97465027d79f77ffce348b935d7"
auth_token = "3a88ff3ccefd35b14108f759e0992cf3"

parameters = {
    "lat": 25.594095,
    "lon": 85.137566,
    "appid": api_key,
    "exclude": "currently,minutely,daily",
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(data['current']['weather'][0]['id'])

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        # print('Bring un umbrella')
        will_rain = True

# print(condition_code)

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to be rain, Remember to bring ☔️",
        from_="+17312074677",
        to="+918540928489"

    )

print(message.status)
# print(message.sid)
