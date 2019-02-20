import requests, json

print("Enter the name of the GitHub user: ")
username = input()

repo = requests.get('https://api.github.com/users/%s/repos' % username).json()
for element in repo:
    name = element['name']
    print(name)
