import requests


def get_channel():
    url = 'https://api.thingspeak.com/channels/9/feeds.json'
    params = {
        'results': 20
    }
    r = requests.get(url, params=params)
    data = r.json()
    feeds = data['feeds']
    index = 1
    feed_data = {}
    light_feeds = []
    temperature_feeds = []
    for feed in feeds:
        light_feed = {
            'home': index,
            'value': round(float(feed['field1']), 2)
        }
        light_feeds.append(light_feed)
        temperature_feed = {
            'home': index,
            'value': round(float(feed['field2']), 2)
        }
        temperature_feeds.append(temperature_feed)
        index += 1
    feed_data['light'] = light_feeds
    feed_data['temperature'] = temperature_feeds
    feed_data['results'] = params['results']
    return feed_data
