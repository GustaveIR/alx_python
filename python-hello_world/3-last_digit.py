#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number using modulo 10
last_digit = abs(number) % 10

# Determine the appropriate suffix for the last digit
if last_digit > 5:
    suffix = "and is greater than 5"
elif last_digit == 0:
    suffix = "and is 0"
else:
    suffix = "and is less than 6 and not 0"

# Print the result
print(f"Last digit of {number} is {last_digit} {suffix}")
