def affine_encrypt(text):
    result = ""
    a = 17
    b = 20
    for char in text:
        if char.isupper():
            result += chr(((a * (ord(char) - 65)) + b) % 26 + 65)
        elif char == ' ':
            result += ' '
        else:
            result += chr(((a * (ord(char) - 97)) + b) % 26 + 97)
    return result

def affine_decrypt(cipher):
    result = ""
    a = 17
    b = 20
    for char in cipher:
        if char.isupper():
            result += chr(((ord(char) - 65 - b) * pow(a, -1, 26)) % 26 + 65)
        elif char == ' ':
            result += ' '
        else:
            result += chr(((ord(char) - 97 - b) * pow(a, -1, 26)) % 26 + 97)
    return result

# Example usage
text = "AFFINE CIPHER"
cipher = affine_encrypt(text)
print("Encrypted message:", cipher)
print("Decrypted message:", affine_decrypt(cipher))
