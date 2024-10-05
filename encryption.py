
def encryption(plain_text, shift):
    encrypted_text = ""
    for char in plain_text.upper():
        # finds the ascii value of character
        ascii_value = ord(char)
        # checks if it is within the ascii value of A and Z
        if ascii_value in range(65, 90+1):
            new_char = 65 + (ascii_value - 65 + shift) % 26
            encrypt = chr(new_char)
            encrypted_text = encrypted_text + encrypt
        else:
            encrypted_text += char
    return encrypted_text


def decryption(plain_text, cipher_text):
    decrypted_text = ""
    for char in plain_text.upper():
        ascii_value = ord(char)
        if ascii_value in range(90, 64, -1):
            new_char = 65 + ((ascii_value - 65) - cipher_text) % 26
            decrypt = chr(new_char)
            decrypted_text = decrypted_text + decrypt
        else:
            decrypted_text += char
    return decrypted_text


Action = input("Do you want to carry out encryption(E) or decryption(D): ")
if Action.upper() == 'E':
    user = input("Enter a text to encrypt:")
    shift_value = int(input("Shift/Key(Number):"))
    shifted_cipher_text = encryption(user, shift_value)
    print(f"Encrypted cipher text: {shifted_cipher_text}")
elif Action.upper() == 'D':
    user = input("Enter the text to decrypted:")
    shift_value = int(input("Shift/Key(Number):"))
    decrypted_plain_text = decryption(user, shift_value)
    print(f"Decrypted text: {decrypted_plain_text}")
else:
    print("Invalid Input!")

