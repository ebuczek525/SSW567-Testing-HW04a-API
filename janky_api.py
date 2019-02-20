import requests, json
from collections import Counter

print("Enter the name of the GitHub user: ")
username = input()

repo = requests.get('https://api.github.com/users/%s/repos' % username).json()

for element in repo:
    name = element['name']
    json_obj = requests.get('https://api.github.com/repos/%s/%s/commits' % (username, name).json()

d = Counter(player['sha'] for player in json_obj)

print("Repo:",name,", Number of commits:",len(d))
