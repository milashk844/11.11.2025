def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False

    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)

    if has_digit and has_upper and has_lower:
        return True
    else:
        return False


print(is_strong_password("Abcderg86"))  # Password is strong! → True
print(is_strong_password("abcdefg"))  # Password not strong! → False

