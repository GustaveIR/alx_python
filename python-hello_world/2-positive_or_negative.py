#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Check if the number is greater than 0, equal to 0, or less than 0, and print the corresponding message
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
