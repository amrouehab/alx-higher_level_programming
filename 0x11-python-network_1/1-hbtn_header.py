#!/usr/bin/python3
"""Script that takes in a URL and displays the value of X-Request-Id"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
