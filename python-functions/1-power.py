def pow(a, b):
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
