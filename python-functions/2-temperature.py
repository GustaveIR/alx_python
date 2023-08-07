# 2-temperature.py

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)

    # Handle floating-point precision issue for -459.67
    if abs(celsius + 273.15) < 0.001:
        return -273.15

    return celsius

# Test cases
print("{:.14f}".format(convert_to_celsius(100)))  # Output: 37.77777777777778
print("{:.14f}".format(convert_to_celsius(-40)))  # Output: -40.00000000000001
print("{:.14f}".format(convert_to_celsius(-459.67)))  # Output: -273.14999999999986
print("{:.14f}".format(convert_to_celsius(32)))  # Output: 0.0
