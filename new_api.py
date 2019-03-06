import json
import unittest
import requests
from unittest.mock import patch

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

    @patch('requests.get')
    def test_apiFunction(self, mocked):
        mocked.side_effect = 'hellogitworld: 30, helloworld: 6, Mocks: 9, Project1: 2, threads-of-life: 1'
        
        api = apiFunction('richkempinski')
        self.assertGreater(len(api), 0)

    @patch('requests.get')
    def test_getRepos(self, mocked):
        mocked.side_effect = 'hellogitworld, helloworld, Mocks, Project1, threads-of-life'
        
        repos = getRepos('richkempinski')
        self.assertGreater(len(repos), 0)
    
    @patch('requests.get')
    def test_getCommits(self, mocked):
        mocked.side_effect = '30'
        
        commits = getCommits('richkempinski', 'hellogitworld')
        self.assertGreater(len(commits), 0)


if __name__ == "__main__":
    print('Running unit tests')
    unittest.main()
