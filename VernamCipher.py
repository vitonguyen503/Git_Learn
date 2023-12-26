import random

def generate_random_key(length):
    """Generate a random key of the specified length."""
    return ''.join([chr(random.randint(65, 90)) for _ in range(length)])

def vernam_encrypt(plain_text, key):
    """Encrypt plaintext using the Verman cipher."""
    if len(plain_text) != len(key):
        raise ValueError("Plaintext and key must have the same length")

    encrypted_text = []
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = key[i]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        encrypted_text.append(encrypted_char)

    return ''.join(encrypted_text)

def vernam_decrypt(ciphertext, key):
    """Decrypt ciphertext using the Verman cipher."""
    if len(ciphertext) != len(key):
        raise ValueError("Ciphertext and key must have the same length")

    decrypted_text = []
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted_text.append(decrypted_char)

    return ''.join(decrypted_text)

plaintext = "COLD"
key = "SGPT"
# key = generate_random_key(len(plaintext)) # Key is random so that some character may not be seen
encrypted_text = vernam_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = vernam_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
