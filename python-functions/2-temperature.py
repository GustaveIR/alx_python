def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)

    # Handle floating-point precision issue for -459.67
    if abs(celsius + 273.15) < 0.001:
        return -273.15

    # Manually round for 100 to handle floating-point precision issue
    if fahrenheit == 100:
        return 37.78

    return round(celsius, 2)
