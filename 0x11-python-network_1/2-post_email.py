#!/usr/bin/python3
"""Script that takes URL and email, sends POST request with email parameter"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
