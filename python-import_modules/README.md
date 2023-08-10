# Simple Python Program: Importing and Using a Function

This is a simple Python program that demonstrates how to import a function from a separate file and use it to perform addition.

## Project Structure

- `add_0.py`: Contains the `add` function that performs addition of two numbers.
- `0-add.py`: Imports the `add` function and demonstrates its usage.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the repository directory: `cd alx_python/python-import_modules`
3. Run the program: `python3 0-add.py`

The program will import the `add` function, perform addition of two predefined numbers, and display the result.

## About the `add` Function

The `add` function is defined in the `add_0.py` file. It takes two arguments `a` and `b`, and returns their sum.

```python
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return a + b
