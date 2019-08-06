import requests


def get_channel():
    url = 'https://api.thingspeak.com/channels/9/feeds.json'
    params = {
        'results': 20
    }
    r = requests.get(url, params=params)
    data = r.json()
    feeds = data['feeds']
    return feeds
