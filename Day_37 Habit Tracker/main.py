from datetime import datetime
import requests


today = datetime.now()
today =datetime(year= 2026, month= 1, day= 8)
user_name = "haihara"
token = "harihara007007"
pixela_end_point = "https://pixe.la/v1/users"

user_params ={ "token" : token, 
              "username" : user_name , 
              "agreeTermsOfService" : "yes", 
              "notMinor" : "yes",
              }

#response = requests.post(url= pixela_end_point, json= user_params)
#print(response.text)

graph_endpoint = f"{pixela_end_point}/{user_name}/graphs"

graph_config = { "id" : "graph1", 
                "name" : "Swimming track", 
                "unit" : "km",
                "type" : "float",
                "color" : "shibafu",
                }

headers = {
    "X-USER-TOKEN" : token
}

#response = requests.post(url= graph_endpoint, json= graph_config, headers= headers)
#data = print(response.text)

#https://pixe.la/v1/users/a-know/graphs/test-graph

pixel_end_point = f"{pixela_end_point}/{user_name}/graphs/graph1"
pixel_config = {"date": today.strftime("%Y%m%d"),
                "quantity":"6.35",
                }


#while True:
#    response = requests.post(url= pixel_end_point, json= pixel_config, headers= headers)
#    if response.json().get("isSuccess"):
#        print("pixel added")
#        break
#    print(response.text)


update_end_point = f"{pixela_end_point}/{user_name}/graphs/graph1/{today.strftime('%Y%m%d')}"
update_config = {"quantity" : "6.35"}

while True:
    response = requests.put(url= update_end_point, json= update_config, headers= headers)
    if response.json().get("isSuccess"):
        print("pixel updated")
        break


#delete works the same

print(response.text)

print(today.strftime("%Y%m%d"))
print(update_end_point)

