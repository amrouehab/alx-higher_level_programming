#!/usr/bin/python3
# Load, add, and save items to a file

import sys
import json

save_to_json_file = __import__('5_save_to_json_file').save_to_json_file
load_from_json_file = __import__('6_load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
