import random
def generate_key(length):
    key = ""
    for i in range(length):
        key += chr(random.randint(0, 255))
    return key
def encrypt(message, key):
    ciphertext = ""
    key_index = 0
    for char in message:
        key_char = key[key_index % len(key)]
        ciphertext += chr(ord(char) ^ ord(key_char))
        key_index += 1
    return ciphertext
def decrypt(ciphertext, key):
    message = ""
    key_index = 0
    for char in ciphertext:
        key_char = key[key_index % len(key)]
        message += chr(ord(char) ^ ord(key_char))
        key_index += 1
    return message
key = generate_key(16)  # Generate a random key of length 16
message = "Hello, world!"  # The message to be encrypted
ciphertext = encrypt(message, key)
decrypted_message = decrypt(ciphertext, key)
print("Original message:", message)
print("Encrypted message:", ciphertext)
print("Decrypted message:", decrypted_message)
