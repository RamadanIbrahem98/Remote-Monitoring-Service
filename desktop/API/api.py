import requests

def data_init(sensor: str, timestamp: int = 0):
    url = 'https://remote-monitoring-api.herokuapp.com/readings/'
    readings = 'temperatures'
    if sensor == 'temp':
        url += 'temp'
    elif sensor == 'humidity':
        url += 'humidity'
        readings = 'humidities'
    else:
        return []

    response = requests.get(url,json={"timestamp": timestamp})

    return response.json()[readings]
    