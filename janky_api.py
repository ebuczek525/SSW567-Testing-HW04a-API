import requests, json
from collections import Counter

print("Enter the name of the GitHub user: ")
username = input()
print("Enter the repo commits URL: ")
repourl = input()

repo = requests.get('https://api.github.com/users/%s/repos' % username).json()
json_obj = requests.get(repourl).json()

c = Counter(player['name'] for player in repo)
d = Counter(player['sha'] for player in json_obj)

print(c,", Number of commits: ",len(d))
