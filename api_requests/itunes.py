import requests

resp = requests.get(
    "https://itunes.apple.com/search", params={'term': 'Jack Johnson', 'limit': 5})

data = resp.json()

for result in data['results']:
    print(result['trackName'])
