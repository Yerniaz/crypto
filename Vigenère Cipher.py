import string
def encrypt_vigenere(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                ciphertext += shifted_char.upper()
            else:
                ciphertext += shifted_char
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            shifted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            if char.isupper():
                plaintext += shifted_char.upper()
            else:
                plaintext += shifted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext
plaintext = "Vigenere Cipher"
key = "SECRET"
ciphertext = encrypt_vigenere(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt_vigenere(ciphertext, key)
print("Decrypted Plaintext:", decrypted_plaintext)
