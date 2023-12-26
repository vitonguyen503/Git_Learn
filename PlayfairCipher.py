def generate_playfair_matrix(key):
    key = key.replace("J", "I")  # Replace J with I for simplicity
    key = key.upper()
    key = ''.join(dict.fromkeys(key))  # Remove duplicate characters
    key += ''.join(chr(65 + i) for i in range(26) if chr(65 + i) not in key)  # Add remaining characters
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def find_letter(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    ciphertext = ''
    plaintext = plaintext.replace("J", "I")  # Replace J with I
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")  # Remove spaces

    # If the length of plaintext is odd, add a padding character
    for i in range(0, len(plaintext) - 1):
        if plaintext[i] == plaintext[i + 1]:
            plaintext = plaintext[:i + 1] + 'X' + plaintext[i+1:]


    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]

    for digraph in plaintext:
        row1, col1 = find_letter(matrix, digraph[0])
        row2, col2 = find_letter(matrix, digraph[1])

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ''
    ciphertext = ciphertext.upper()
    ciphertext = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]

    for digraph in ciphertext:
        row1, col1 = find_letter(matrix, digraph[0])
        row2, col2 = find_letter(matrix, digraph[1])

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    # Remove redundant character 'X'
    for i in range(1, len(plaintext) - 1):
        if plaintext[i] == 'X' and plaintext[i + 1] == plaintext[i - 1]:
            plaintext = plaintext[:i] + plaintext[i+1:]
    return plaintext

plaintext = "COMMUNICATE"
key = "COMPUTER"

encrypted = playfair_encrypt(plaintext, key)
decrypted = playfair_decrypt(encrypted, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
