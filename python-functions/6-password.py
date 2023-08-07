# 6-password.py

def validate_password(password):
    # Check for password length
    if len(password) < 8:
        return False

    # Check for uppercase letter, lowercase letter, and digit
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    # Check for spaces
    if " " in password:
        return False

    # Check if all conditions are met
    return has_uppercase and has_lowercase and has_digit
