#!/usr/bin/env python3

# Function to compute a^b
def power(a, b):
    if b == 0:
        return 1

    result = 1
    if b > 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result /= a

    return result

pow = __import__('1-power').power

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
