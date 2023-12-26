def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - key) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

text = "TRVJRI TZGYVIJ RIV HLZKV VRJP KF TIRTB"
for i in range(1, 26):
    print(caesar_decrypt(text, i), " Key: ", i)

