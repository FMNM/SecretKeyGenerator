import secrets


def generate_secret_key(length=32):
    # Generates a URL-safe, secure random string of the given length (in bytes).
    # Each byte is converted to roughly 1.3 characters, so the final string length is longer.
    return secrets.token_urlsafe(length)


# Example usage
secret_key = generate_secret_key()
print(secret_key)
