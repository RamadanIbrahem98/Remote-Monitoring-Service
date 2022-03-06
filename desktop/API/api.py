import requests


def fetch_data(sensor: str, timestamp: int = 0):
    url = 'https://remote-monitoring-api.herokuapp.com/readings/'
    readings = 'temperatures'
    if sensor == 'temp':
        url += 'temp'
    elif sensor == 'humidity':
        url += 'humidity'
        readings = 'humidities'
    else:
        return []

    response = requests.get(url, json={"timestamp": timestamp})

    if response.status_code != 200:
        return []

    return response.json()[readings]


def set_alarm(is_set):
    url = 'https://remote-monitoring-api.herokuapp.com/control/alarm/'
    response = requests.post(url, json={"is_set": is_set})
    if response.status_code != 200:
        return False
    return True


def get_alarm():
    url = 'https://remote-monitoring-api.herokuapp.com/control/alarm/'
    response = requests.get(url)
    if response.status_code != 200:
        return False
    return response.json()['alarm']
