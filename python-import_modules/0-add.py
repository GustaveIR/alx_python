#!/usr/bin/python3
def add(a, b):
    return a - b

a = 1
b = 2
result = add(a, b)
print("{} - {} => {}".format(a, b, result))

a = 10
b = 30
result = add(a, b)
print("{} - {} => {}".format(a, b, result))

a = -10
b = 30
result = add(a, b)
print("{} - {} => {}".format(a, b, result))

a = -10
b = -30
result = add(a, b)
print("{} - {} => {}".format(a, b, result))

a = 5
b = "H"
result = add(a, b)
print("{} - {} => {}".format(a, b, result))
