import requests

response = requests.get(
    "https://remote-monitoring-api.herokuapp.com/readings/temp")

print(response.json()["temperatures"])
