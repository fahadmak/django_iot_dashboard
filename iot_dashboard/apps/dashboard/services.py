import requests


def get_channel():
    url = 'https://api.thingspeak.com/channels/9/feeds.json'
    params = {
        'timescale': 5
    }
    r = requests.get(url, params=params)
    data = r.json()
    channel = data['feeds']
    return channel
