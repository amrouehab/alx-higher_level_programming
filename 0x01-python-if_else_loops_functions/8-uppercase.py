#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Check if the character is lowercase (ASCII between 97 and 122)
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32
            char = chr(ord(char) - 32)
        # Print the character without a newline, followed by an empty space
        print("{}".format(char), end="")
    print()  # Print a newline at the end
