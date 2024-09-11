#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Compute the last digit
last_digit = abs(number) % 10

# Determine the appropriate message
if last_digit > 5:
    message = f"Last digit of {number} is {last_digit} and is greater than 5"
elif last_digit == 0:
    message = f"Last digit of {number} is {last_digit} and is 0"
else:
    message = f"Last digit of {number} is {last_digit} and is less than 6 and not 0"

print(message)
