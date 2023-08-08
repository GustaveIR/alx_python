# 0-add.py

# Define the variables a and b
a = 1
b = 2

if __name__ == "__main__":
    # Import the add function from add_0.py
    from add_0 import add

    # Calculate the result of the addition using the add function
    result = add(a, b)

    # Print the result in the desired format
    print("{} + {} = {}".format(a, b, result))
