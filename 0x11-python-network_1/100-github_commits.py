#!/usr/bin/python3
"""Script that lists 10 commits of a repository"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            sha = commits[i].get('sha')
            name = commits[i].get('commit').get('author').get('name')
            print(f"{sha}: {name}")
    except IndexError:
        pass
