import requests
from twilio.rest import Client



w_api = "https://api.openweathermap.org/data/2.5/forecast"

acc_sid = "ACaebd41d636800afb03703d8cc17e23c2"
auth_tokn = "053dbd94d5f58195e056a7934f5f3d4d"

weather_parameters = {"appid" : "abaaf91a82b94eb1c1efdfebe82925f2",
                       "lat" : 17.74,
                         "lon" : 83.34,
                         "units": "metric",
                         "cnt" : 4
                         }

response = requests.get(w_api, params= weather_parameters )
response.raise_for_status()

data = response.json()

weather_id = data["list"][0]["weather"][0]["id"]
print(weather_id)

weather_ids = [item["weather"][0]["id"] for item in data["list"]]
print(type(weather_ids[0]))

weather_ids.append(656)


if any(id < 700 for id in weather_ids) :
        print("Bring Umbrella")
        account_sid = "ACaebd41d636800afb03703d8cc17e23c2"
        auth_token = "053dbd94d5f58195e056a7934f5f3d4d"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Hey bujji, just a test message from code, love you :)",
            from_="+16825028861",
            to="+918586896848",
        )

        print(message.body)

    



