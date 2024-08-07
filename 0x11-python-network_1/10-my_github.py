#!/usr/bin/python3
"""
A script that:
- takes your GitHub credentials (username and personal access token)
- uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print(f"Error: Unable to fetch user ID (status code: {response.status_code})")
