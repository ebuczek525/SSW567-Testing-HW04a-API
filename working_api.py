import requests
import json
import unittest

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
        self.assertGreater(len(apiFunction('richkempinski'), 0))

    def test_getRepos(self):
        self.assertGreater(len(getRepos('richkempinski'), 0))

    def test_getCommits(self):
        self.assertGreater(getCommits('richkempinski', 'hellogitworld'), 0)


if __name__ == "__main__":
    print('Running unit tests')
    unittest.main()
