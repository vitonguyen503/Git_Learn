def vigenere_encrypt(plain_text, key):
    encrypted_text = []
    key_length = len(key)
    key = key.upper()

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key_length = len(key)

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

plaintext = "HELLO"
key = "KEY"
encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
