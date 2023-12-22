def check_password_validity(password):
    if not password:
        return -1
    if len(password) < 8:
        return 0
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = '@' in password
    if not (has_lowercase and has_uppercase and has_digit and has_special):
        return 0
    return 1
print(check_password_validity("abcd"))
print(check_password_validity("aBcD@123456"))
print(check_password_validity("_aHkL&098765"))
print(check_password_validity("   ka   "))
