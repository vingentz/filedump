#!/usr/bin/python3
"""script that takes GitHub username and password and uses the GitHub API
to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    k = requests.get("https://api.github.com/user", auth=auth)
    print(k.json().get("id"))
