import random

# Function to compute modular exponentiation (a^b mod p)
def mod_exp(a, b, p):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p
        a = (a * a) % p
        b //= 2
    return result

def mod_inverse(x, p):
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = extended_gcd(x, p)

    if g != 1:
        # Modular inverse doesn't exist
        return None
    else:
        return x % p

def generate_keys():
    p = 19  # Replace with a larger prime for stronger security
    g = 11  # A primitive root modulo p

    x = 3 # random.randint(2, p - 2)

    h = mod_exp(g, x, p)

    return (p, g, h, x)

def encrypt(plaintext, p, g, h):
    # Generate a random session key (y)
    y = 5 # random.randint(2, p - 2)

    # Compute c1 = g^y mod p
    c1 = mod_exp(g, y, p)

    # Compute s = h^y mod p
    s = mod_exp(h, y, p)

    # Encrypt the plaintext
    ciphertext = mod_exp(plaintext * s, 1, p)

    return c1, ciphertext

def decrypt(c1, ciphertext, p, x):
    # Compute the session key s = c1^a mod p
    s = mod_exp(c1, x, p)
    s_inverse = mod_inverse(s, p)
    print(s_inverse)

    # Decrypt the ciphertext
    plaintext = mod_exp(ciphertext * s_inverse, 1, p)
    return plaintext

if __name__ == "__main__":
    p, g, h, x = generate_keys()

    message = 10 # Plaintext has to be less than P (selected prime number)
    print("Plaintext:", message)

    print("Test: ", mod_inverse(7, 19))

    # Encrypt the message
    c1, c2 = encrypt(message, p, g, h)
    print("Ciphertext (c1, c2):", c1, c2)

    # Decrypt the message
    decrypted_message = decrypt(c1, c2, p, x)
    print("Decrypted Message:", decrypted_message)
