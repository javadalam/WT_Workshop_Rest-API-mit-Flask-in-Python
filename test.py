import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+"people/Javad Alamdar/32")

# response = requests.post(BASE+"people/Javad Alamdar/32")

print(response.json())