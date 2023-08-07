# 0-add.py

# Define the variables a and b
a = 1
b = 2

# Import the add function from add_0.py
from add_0 import add

# Calculate the result of the addition using the add function
result = add(a, b)

# Print the result in the desired format
print("{} + {} = {}".format(a, b, result))

# Correct output - case: a = 1 and b = 2 FAKE add() => a - b
print("Correct output - case: a = {} and b = {} FAKE add() => {} - {}".format(a, b, a, b))

# Correct output - case: a = 10 and b = 30 FAKE add() => a - b
a = 10
b = 30
result = add(a, b)
print("Correct output - case: a = {} and b = {} FAKE add() => {} - {}".format(a, b, a, b))

# Correct output - case: a = -10 and b = 30 FAKE add() => a - b
a = -10
b = 30
result = add(a, b)
print("Correct output - case: a = {} and b = {} FAKE add() => {} - {}".format(a, b, a, b))

# Correct output - case: a = -10 and b = -30 FAKE add() => a - b
a = -10
b = -30
result = add(a, b)
print("Correct output - case: a = {} and b = {} FAKE add() => {} - {}".format(a, b, a, b))

# Correct output - case: a = 5 and b = "H" FAKE add() => a - b , here are the errors , please help to fix them
a = 5
b = "H"
result = add(a, b)
print("Correct output - case: a = {} and b = {} FAKE add() => {} - {}".format(a, b, a, b))
