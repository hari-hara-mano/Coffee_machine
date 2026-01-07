import requests

responce = requests.get("http://api.open-notify.org/iss-now.json")
responce.raise_for_status()

data = responce.json()
print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"] 

satillite_pos =(longitude, latitude)
print(satillite_pos)
