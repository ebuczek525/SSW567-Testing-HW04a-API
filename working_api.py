import requests, json, unittest

print("Enter the name of the GitHub user: ")
username = input()

def apiFunction(username):
    repos = getRepos(username)
    dict = {}
    for repo in repos:
        name = repo["name"]
        dict[name] = getCommits(username, name)

    return dict
        

def getRepos(username):
    r = requests.get('https://api.github.com/users/' + username + '/repos');
    data = r.json()  
    return data

def getCommits(username, name):
    r = requests.get('https://api.github.com/repos/' + username + '/' + name + '/commits');
    data = r.json()
    return len(data)

class TestapiFunction(unittest.TestCase):
    def test_apiFunction(self):
        assert len(apiFunction('ebuczek525')) > 0

    def test_getRepos(self):
        assert len(getRepos('ebuczek525')) > 0

    def test_getCommits(self):
        assert getCommits('ebuczek525', 'SSW567-Testing-HW02a') = 10


if __name__ == "__main__":
    print('Running unit tests')
    unittest.main()
