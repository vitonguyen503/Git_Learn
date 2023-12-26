import random

def euler_phi(n):
    phi = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            phi += 1
    return phi

def coprime_numbers_with_n(n):
    coprimes = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def is_primitive_root(a, n, phi_n):
    factors = prime_factors(phi_n)
    for p in factors:
        if pow(a, phi_n // p, n) == 1:
            return False
    return True

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return set(factors)

def select_primitive_root(primitive_roots):
    while True:
        for i, root in enumerate(primitive_roots):
            print(f"{i + 1}. {root}")

        choice = input("Chọn một căn nguyên thủy (1, 2, ...) hoặc nhấn Enter để thoát: ")
        if choice == "":
            return None  # Người dùng không chọn gì, trả về None
        try:
            index = int(choice) - 1
            if 0 <= index < len(primitive_roots):
                return primitive_roots[index]  # Trả về căn nguyên thủy được chọn
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


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

# def check_primitive_root(a, b):
#     ngto_cung_nhau = [], primitive_root = []
#     for i in range (1, a):
#         if(is_prime(i, a)):
#             ngto_cung_nhau.append(i)
#     for tmp in ngto_cung_nhau:
#         tmp_list = set()
#         for i in range (1, len(ngto_cung_nhau)):
#             tmp_list.add()

while True:
    p = int(input("Enter p: ")) # 353
    phi_n = euler_phi(p)
    print(f"Các số nguyên tố cùng nhau với {p} là:")
    coprimes = coprime_numbers_with_n(p)
    print(coprimes)
    primitive_roots = []
    for a in coprimes:
        if is_primitive_root(a, p, phi_n):
            primitive_roots.append(a)
    if len(primitive_roots) > 0:
        print(f"Các căn nguyên thủy của {p} là:")
        print(primitive_roots)
        break
    else:
        print("p doesnt have primitive root! ")


g = select_primitive_root(primitive_roots)

    # g = int(input("Enter g: ")) # 3

alice_private_key = int(input()) # random.randint(1, p - 1)
bob_private_key = int(input()) # random.randint(1, p - 1)

print("Alice's private key:", alice_private_key, "\nBob's private key:", bob_private_key)

# Function to compute public key
def compute_public_key(private_key):
    return (g ** private_key) % p

alice_public_key = compute_public_key(alice_private_key)
bob_public_key = compute_public_key(bob_private_key)
print("\nAlice's public key:", alice_public_key, "\nBob's public key:", bob_public_key)

# Alice and Bob exchange public keys

# Shared secret computation
shared_secret_alice = (bob_public_key ** alice_private_key) % p
shared_secret_bob = (alice_public_key ** bob_private_key) % p

# Both Alice and Bob now have the same shared secret, which can be used for encryption/decryption.
print("\nShared Secret (Alice):", shared_secret_alice)
print("Shared Secret (Bob):", shared_secret_bob)
