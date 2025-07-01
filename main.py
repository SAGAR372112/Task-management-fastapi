import secrets

def generate_token(length=32):
    return secrets.token_hex(length)

# Example usage
if __name__ == '__main__':
    token = generate_token()
    print("Generated Token:", token)