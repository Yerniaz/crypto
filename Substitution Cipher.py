def substitution_cipher(text, key, decrypt=False):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if decrypt:
        alphabet, key = key, alphabet
    result = ""
    for letter in text:
        if letter.lower() in alphabet:
            substitute_char = key[alphabet.find(letter.lower())]
            if letter.isupper():
                result += substitute_char.upper()
            else:
                result += substitute_char
        else:
            result += letter
    return result
key = "fcpevqkzgmtrayonujdlwhbxsi"
text = "On a dark desert highway Cool wind in my hair"
encoded_text = substitution_cipher(text, key)
print(encoded_text)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DECODE !!!!!!!!!!!!!!!!!!!!
print('!!!!DECODING!!!!!!!')
encoded_text = "Oy f efjt evdvjl zgkzbfs Poor bgye gy as zfgj"

decoded_text = substitution_cipher(encoded_text, key, decrypt=True)
print(decoded_text)
