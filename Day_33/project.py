import requests
import datetime


time_now = datetime.datetime.now()
print("\n"*5)
print(time_now.hour)
latitude = 11.6770504
longitude = 92.7217198
#date = "1995-12-14"

parameters = {
    "lng": longitude,
    "lat": latitude
    
}
response = requests.get("https://api.sunrise-sunset.org/json?lat=11.6770504&lng=92.7217198&formatted=0")
response.raise_for_status()

data = response.json()


sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print("\n"*5)
print(sunrise, sunset)

