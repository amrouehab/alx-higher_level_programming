#!/usr/bin/python3
# Loop through the ASCII values for lowercase letters
for char in range(97, 123):
    if chr(char) != 'q' and chr(char) != 'e':
        print(chr(char), end="")
