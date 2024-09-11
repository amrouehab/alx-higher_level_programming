#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Calculate the last digit with its sign
last_digit = number % 10 if number >= 0 else (-number % 10) * -1

# Print the last digit with the correct format
print(f"Last digit of {number} is {last_digit}", end="")

# Check the last digit and print the appropriate message
if last_digit > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
