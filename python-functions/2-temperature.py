def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)

    # Handle floating-point precision issue for -459.67
    if abs(celsius + 273.15) < 0.001:
        return -273.15

    # Round to two decimal places for other values
    return round(celsius, 2)
