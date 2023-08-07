# 4-fibonacci.py

def fibonacci_sequence(n):
    if n <= 0:
        return []

    fib_seq = [0, 1]

    while len(fib_seq) < n:
        next_number = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_number)

    return fib_seq
