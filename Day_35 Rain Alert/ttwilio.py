import requests
from twilio.rest import Client


account_sid = "ACaebd41d636800afb03703d8cc17e23c2"
auth_token = "053dbd94d5f58195e056a7934f5f3d4d"


W_API = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": 17.74,
    "lon": 83.34,
    "appid": "abaaf91a82b94eb1c1efdfebe82925f2",
    "units": "metric",
    "cnt": 4
}

response = requests.get(W_API, params=params)
response.raise_for_status()
data = response.json()

weather_ids = [item["weather"][0]["id"] for item in data["list"]]

weather_ids.append(500)

if any(wid < 700 for wid in weather_ids):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Rain expected. Carry an umbrella ☔",
        from_="+16825028861",
        to="+918686886848"
    )
    print(message.status)
