# Implement password_strength(password). 
# Return Weak if the password has fewer than 8 characters. 
# Return Medium if it has at least 8 characters but does not contain both letters and digits. 
# Return Strong if it has at least 8 characters and contains at least one letter and at least one digit. 
# Students may need to research isalpha and isdigit.

def password_strength(password):
    if len(password) < 8:
        return "Weak"

    seen_alpha = False
    seen_digit = False

    for char in password:
        if char.isalpha():
            seen_alpha = True
        elif char.isdigit():
            seen_digit = True

    # If both booleans result in True, password will always be "Strong"
    if seen_alpha and seen_digit:
        return "Strong"
    else:
        # When the guard clause for "Weak" password does not fire and --
        # -- both booleans aren't true at the same time (which should result in strong) --
        # -- The password would therefore be "Medium" since it's neither "Weak" nor "Strong"
        return "Medium"

print(password_strength("abc12345"))
print(password_strength("abcdefgh"))
print(password_strength("abc12"))