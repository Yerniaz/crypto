def shift_cipher(text, shift):
    text = text.upper()
    result = ""
    for char in text:
        if char.isalpha():
            ascii_code = ord(char)
            shifted_ascii_code = ascii_code + shift
            if shifted_ascii_code > ord('Z'):
                shifted_ascii_code -= 26
            elif shifted_ascii_code < ord('A'):
                shifted_ascii_code += 26
            result += chr(shifted_ascii_code)
        else:
            result += char
    return result
plaintext = "Hello, World! My name is Yerniyaz"
shift = 3
ciphertext = shift_cipher(plaintext, shift)
print(ciphertext)
# DECODING
print('!!!!!!!!!!!!!!!!!!!!!!!DECODING!!!!!!!!!!!!!!!!!!!')
ciphertext = "KHOOR, ZRUOG! PB QDPH LV BHUQLBDC"
shift = -3
plaintext = shift_cipher(ciphertext, shift)
print(plaintext)
