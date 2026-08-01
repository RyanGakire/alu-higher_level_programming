#!/usr/bin/python3
"""Displays the GitHub id of a user authenticated with Basic Auth."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (sys.argv[1], sys.argv[2])
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
