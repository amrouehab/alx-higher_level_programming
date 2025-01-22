#!/usr/bin/python3
"""Script that sends POST request to search API"""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}
    
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        response = r.json()
        if response:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
