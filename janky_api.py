import requests, json
from collections import Counter

print("Enter the name of the GitHub user: ")
username = input()

def apiFunction(username):
    repos = requests.get('https://api.github.com/users/' + username + '/repos');
    repodata = repos.json()
    name = Counter(player['name'] for player in repodata)
    commits = requests.get('https://api.github.com/repos/' + username + '/' + name + '/commits');
    commitdata = commits.json()
    numcommits = Counter(player['commit'] for player in commitdata)

    return (name,len(numcommits))

#print("Repo:",name,", Number of commits:",len(commits))
