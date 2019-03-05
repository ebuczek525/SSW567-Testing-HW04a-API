import json
import unittest
import requests
from unittest import mock
import patch

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
    @mock.patch('requests.get')

    def test_apiFunction(self, mockedReq):
        mockedReq.return_value = ('hellogitworld: 30, helloworld: 6, Mocks: 9, Project1: 2, threads-of-life: 1')
        api = apiFunction(self.username)
        self.assertGreater(len(apiFunction), 0)

    def test_getRepos(self, mockedReq):
        mockedReq.return_value = ('hellogitworld, helloworld, Mocks, Project1, threads-of-life')
        repos = getRepos(self.username)
        self.assertGreater(len(getRepos), 0)

    def test_getCommits(self, mockedReq):
        mockedReq.return_value = ('30')
        commits = getCommits(self.username, self.reponame)
        self.assertGreater(len(getCommits), 0)


if __name__ == "__main__":
    print('Running unit tests')
    unittest.main()