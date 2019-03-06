import json
import unittest
import requests
from unittest.mock import MagicMock

def apiFunction(username):
    repos = getRepos(username)
    dict = {}
    for repo in repos:
        reponame = repo["name"]
        dict[reponame] = getCommits(username, reponame)

    return dict

def getRepos(username):
    r = requests.get('https://api.github.com/users/' + username + '/repos')
    data = r.json()
    return data

def getCommits(username, reponame):
    r = requests.get('https://api.github.com/repos/' + username + '/' + reponame + '/commits')
    data = r.json()
    return len(data)


class TestapiFunction(unittest.TestCase):

    def test_apiFunction(self):
        mock = MagicMock()
        mock.__str__.return_value = '[hellogitworld: 30, helloworld: 6, Mocks: 9, Project1: 2, threads-of-life: 1]'
        self.assertEqual(str(mock), [hellogitworld: 30, helloworld: 6, Mocks: 9, Project1: 2, threads-of-life: 1])

    def test_getRepos(self):
        mock = MagicMock()
        mock.__str__.return_value = '[hellogitworld, helloworld, Mocks, Project1, threads-of-life]'
        self.assertEqual(str(mock), [hellogitworld, helloworld, Mocks, Project1, threads-of-life])
    
    def test_getCommits(self):
        mock = MagicMock()
        mock.__str__.return_value = '30'
        self.assertEqual(str(mock), 30)


if __name__ == "__main__":
    print('Running unit tests')
    unittest.main()
