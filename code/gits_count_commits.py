import helper
import requests
import json


def count_user_commits(user, repo_name):
    r = requests.get('https://api.github.com/users/%s/repos' % user)
    repos = json.loads(r.content)

    for repo in repos:
        if repo['fork'] is True:
            continue
        temp = repo['name'] + '.git'
        if temp == repo_name:
            n = count_repo_commits(repo['url'] + '/commits')
            repo['num_commits'] = n
            yield repo


def count_repo_commits(commits_url, _acc=0):
    r = requests.get(commits_url)
    commits = json.loads(r.content)
    n = len(commits)
    if n == 0:
        return _acc
    link = r.headers.get('link')
    if link is None:
        return _acc + n
    next_url = find_next(r.headers['link'])
    if next_url is None:
        return _acc + n
    return count_repo_commits(next_url, _acc + n)


def find_next(link):
    for l in link.split(','):
        a, b = l.split(';')
        if b.strip() == 'rel="next"':
            return a.strip()[1:-1]


def count_commits(args):
    total = 0
    info = helper.get_repo_name()
    username = info[0][15:]
    repo_ = info[1]
    for repo in count_user_commits(username, repo_):
        total += repo['num_commits']
    print("Total commits: %d" % total)
