#!/usr/bin/python3

for i in range(100):
    # Print the number with leading zeros and format the output
    # Use a single print function and end it with ", " if it's not the last number
    print(f"{i:02}", end=", " if i < 99 else "\n")
