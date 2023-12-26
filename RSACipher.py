import math

def check_prime_number(num):
    if num < 2:
        return False
    sqrt_num = (int)(math.sqrt(num))
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            return False
    return True

def is_prime(p, q):
    return True if gcd(p, q) == 1 else False

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

while True:
    print("Enter p, q: (p, q must be prime numbers)")
    p = int(input()) #73
    q = int(input()) #151
    if check_prime_number(p) and check_prime_number(q):
        break
    else:
        print("p or q is not prime! Please enter again!")

# Calculate n, φ(n), d (modular multiplicative inverse of e modulo φ(n))
n = p * q
phi_n = (p - 1) * (q - 1)

while True:
    e = int(input("Enter e (gcd(e, phi_n) must be 1): ")) #11
    if is_prime(phi_n, e):
        break
    else:
        print("GCD(phi_n, e) is not 1! Please enter e again!")

d = pow(e, -1, phi_n)

if d < 0:
    d += phi_n

print("phi_n:", phi_n, "d:", d)

def encrypt_rsa(plaintext, e, n):
    ascii_plaintext = []
    for char in plaintext:
        ascii_plaintext.append(ord(char))

    # Encrypt the integer
    ciphertext = []
    for i in ascii_plaintext:
        ciphertext.append(pow(i, e, n))

    return ciphertext

def decrypt_rsa(ciphertext, d, n):
    ascii_plaintext = []
    for i in ciphertext:
        ascii_plaintext.append(pow(i, d, n))

    plaintext = []
    for i in ascii_plaintext:
        plaintext.append(chr(i))

    return ''.join(plaintext)

if not is_prime(p, q):
    print("Invalid p, q. Please adjust these number!")
    exit()

plaintext = "How are you?"
print("Plaintext: ", plaintext)

ciphertext = encrypt_rsa(plaintext, e, n)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt_rsa(ciphertext, d, n)
print("Decrypted Text:", decrypted_text)
