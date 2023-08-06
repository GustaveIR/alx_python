#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Check if the number is an integer
if isinstance(number, int):
    # Check if the number is positive, negative, or zero, and print the corresponding message
    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")
else:
    print(f"Error: The generated number '{number}' is not an integer.")
