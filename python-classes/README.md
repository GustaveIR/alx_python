# 0. Square with size

Write a class `Square` that defines a square by:

- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)

You are not allowed to import any module.

## Why?

Why is `size` a private attribute?

The size of a square is crucial for a square, many things depend on it (area computation, etc.), so you, as the class builder, must control the type and value of this attribute. One way to have control is to keep it private. You will see in the next tasks how to get, update, and validate the size value.

## Example Usage

```python
#!/usr/bin/python3
Square = __import__('0-square').Square

mysquare = Square(3)
print(type(mysquare))  # Output: <class '0-square.Square'>
print(mysquare.__dict__)  # Output: {'_Square__size': 3}

mysquare = Square(89)
print(type(mysquare))  # Output: <class '0-square.Square'>
print(mysquare.__dict__)  # Output: {'_Square__size': 89}

try:
    print(mysquare.size)
except Exception as e:
    print(e)  # Output: 'Square' object has no attribute 'size'

try:
    print(mysquare._Square__size)
except Exception as e:
    print(e)  # Output: 89
