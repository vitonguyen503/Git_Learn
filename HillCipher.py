import numpy as np
from sympy import Matrix
from sympy import mod_inverse
import math

def adjoint_matrix(matrix):
    n = len(matrix)
    adjoint = np.zeros((n, n), dtype=float)

    for i in range(n):
        for j in range(n):
            # Calculate the cofactor for each element
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactor = ((-1) ** (i + j)) * np.linalg.det(minor)

            # Place the cofactor in the corresponding position in the adjoint matrix
            adjoint[j, i] = (cofactor % 26)  # Transpose the indices here

    adjoint = np.round(adjoint).astype(int)

    return adjoint

def matrix_inverse_mod(matrix, modulus):
    n = matrix.shape[0]  # Get the size of the matrix (number of rows)

    # Calculate the determinant of the matrix
    determinant = int(np.linalg.det(matrix)) % modulus # OK

    if determinant != 0:
        # Calculate the adjoint matrix
        adj_matrix = adjoint_matrix(matrix) # OK

        # Calculate the modular multiplicative inverse of the determinant modulo 26
        determinant_inverse = mod_inverse(determinant, modulus) # OK

        # Calculate the inverse matrix modulo 26
        inverse_matrix = (adj_matrix * determinant_inverse) % modulus
        print("Inverse matrix: ", inverse_matrix)
        return inverse_matrix
    else:
        raise ValueError("The matrix is not invertible, so no inverse matrix can be generated.")

def key_matrix_generation(key):
    key = key.replace(" ", "").upper()
    key = [ord(char) - ord('A') for char in key]
    m = (int) (math.sqrt(len(key)))
    if m * m != len(key):
        print("Key length is invalid!")
        exit()
    key_matrix = np.array(key).reshape(m, m)
    return key_matrix

def encrypt_hill(plaintext, key_matrix):
    m = len(key_matrix)
    plaintext = plaintext.replace(" ", "").upper()
    plaintext = [ord(char) - ord('A') for char in plaintext]
    while len(plaintext) % m != 0:
        plaintext.append(0)
    plaintext_matrix = np.array(plaintext).reshape(-1, m) # turn array into a matrix with m col and number of rows is auto
    ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    ciphertext = "".join([chr(c + ord('A')) for c in ciphertext_matrix.flatten()])
    return ciphertext

def decrypt_hill(ciphertext, key_matrix):
    m = len(key_matrix)
    key_inverse = matrix_inverse_mod(key_matrix, 26)
    ciphertext = ciphertext.replace(" ", "").upper()
    ciphertext = [ord(char) - ord('A') for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext).reshape(-1, m)
    plaintext_matrix = np.dot(ciphertext_matrix, key_inverse) % 26
    plaintext = "".join([chr(c + ord('A')) for c in plaintext_matrix.flatten()])
    return plaintext

while True:
    key = input("Enter key: ")
    key_matrix = key_matrix_generation(key)
    print("Key matrix:\n" , key_matrix)
    det = int(round(Matrix(key_matrix).det())) % 26
    print(det)
    if det != 0:
        break
    else:
        print("The input matrix is not invertible!")

plaintext = input("Enter plaintext: ")
plain_len = len(plaintext)
ciphertext = encrypt_hill(plaintext, key_matrix)
print("Encrypted:", ciphertext)
decrypted_text = decrypt_hill(ciphertext, key_matrix)
if len(decrypted_text) > plain_len:
    decrypted_text = decrypted_text[:plain_len]
print("Decrypted:", decrypted_text)
