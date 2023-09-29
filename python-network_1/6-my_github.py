#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API to display your id.
Uses Basic Authentication with a personal access token as password.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: {} <username> <token>".format(sys.argv[0]))
    
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/GustaveIR"

    response = requests.get(url, auth=(username, token))
    try:
        json_response = response.json()
        print(json_response.get("id"))
    except ValueError:
        print("None")
