#!/usr/bin/python3
def print_alphabet_exclude():
    for letter in range(ord('a'), ord('z') + 1):
        if chr(letter) not in ['q', 'e']:
            print(chr(letter), end="")
