def power(a, b):
    result = 1
    for _ in range(abs(b)):
        result *= a

    if b < 0:
        result = 1 / result

    return result
