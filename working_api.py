import requests
import json
import unittest

from test1 import a
from test2 import b

def apiFunction(username):
    repos = getRepos(username)
    dict = {}
    for repo in repos:
        reponame = repo["name"]
        dict[reponame] = getCommits(username, reponame)

    return dict
        

def getRepos(username):
    r = requests.get('https://api.github.com/users/' + username + '/repos');
    data = r.json()  
    return data

def getCommits(username, reponame):
    r = requests.get('https://api.github.com/repos/' + username + '/' + reponame + '/commits');
    data = r.json()
    return len(data)

class TestapiFunction(unittest.TestCase):
    def test_apiFunction(self):
        self.assertEqual(apiFunction('richkempinski'), a)

    def test_getRepos(self):
        self.assertEqual(getRepos('richkempinski'), b)

    def test_getCommits(self):
        self.assertEqual(getCommits('richkempinski', 'hellogitworld'), 30)


if __name__ == "__main__":
    print('Running unit tests')
    unittest.main()
