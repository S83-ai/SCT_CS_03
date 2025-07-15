import re

def check_password_strength(password):
    # Criteria checks
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Strength levels
    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])
    
    if score == 5:
        strength = "Very Strong "
    elif score == 4:
        strength = "Strong "
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Output
    return {
        "Password": password,
        "Length OK": not length_error,
        "Uppercase OK": not uppercase_error,
        "Lowercase OK": not lowercase_error,
        "Digit OK": not digit_error,
        "Special Char OK": not special_char_error,
        "Strength": strength
    }

# Example usage
password = input("Enter a password to check: ")
result = check_password_strength(password)

# Display results
for k, v in result.items():
    print(f"{k}: {v}")
