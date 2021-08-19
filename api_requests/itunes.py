import requests

# resp = requests.get(
#     "https://itunes.apple.com/search", params={'term': 'Jack Johnson', 'limit': 5})

# data = resp.json()

# for result in data['results']:
#     print(result['trackName'])

data1 = {
    'username': 'chicken',
    'tweets': ['hello', 'goodbye', 'bock bock', {'id': 1, 'text': 'my first tweet'}]
}

requests.post("https://enfzjd3qh3tfeqs.m.pipedream.net", json=data1)
