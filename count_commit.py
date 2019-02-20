import requests, json
from collections import Counter

url = input()
json_obj = requests.get(url).json()

c = Counter(player['sha'] for player in json_obj)
print(len(c))
