# 1-power.py

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

    # Format the result with one less digit after the decimal point
    formatted_result = "{:.19e}".format(result)

    return float(formatted_result)
