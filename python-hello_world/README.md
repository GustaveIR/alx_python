# Positive or Negative Program

This program generates a random signed number and determines whether it is positive, negative, or zero. It uses conditional statements to print the appropriate message based on the number's value.

## Instructions

1. Clone this repository: `git clone https://github.com/GustaveIR/alx_python.git`
2. Navigate to the "python-hello_world" directory: `cd alx_python/python-hello_world`
3. Run the program: `python3 2-positive_or_negative.py`

## Output Examples
# Test cases
def test_positive_output():
    # Test positive number
    assert "is positive" in capture_output()

def test_negative_output():
    # Test negative number
    assert "is negative" in capture_output()

def test_zero_output():
    # Test zero
    assert "is zero" in capture_output()

def test_wrong_type_output():
    # Test non-integer input
    assert "Error: The generated number" in capture_output()

def capture_output():
    try:
        # Capture the output from the code
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            # Execute the code
            exec(open('python-hello_world').read())
        return f.getvalue()
    except Exception as e:
        return str(e)

# Run the test cases
test_positive_output()
test_negative_output()
test_zero_output()
test_wrong_type_output()
