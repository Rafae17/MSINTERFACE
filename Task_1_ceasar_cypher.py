def caesar_cipher(text, shift, mode):
    result =""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift * mode) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift, 1)

def decrypt(text, shift):
    return caesar_cipher(text, shift, -1)

while True:
    operation = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()

    if operation == 'q' :
        break

    if operation not in ['e', 'd']:
        print("Invalid operation. Please try again.")
        continue

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (1-25): "))

    if operation == 'e':
        result = encrypt(message, shift)
        print(f"Encrypted messages: {result}")
    else:
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")