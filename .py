import requests, json
from collection import Counter

r = requests.get('https://api.github.com/users/richkempinski/repos')
for result in data['results']:
    print("Repo: {}".format(result['name']))
    
url = "https://api.github.com/repos/richkempinski/hellogitworld/commits"
json_obj = requests.get(url).json()
c = Counter(player['sha'] for player in json_obj)
print(len(c))
