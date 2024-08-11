# Implement the Caesar cipher encryption and decryption algorithm.

def encrypt(text, shift):
    result = ""

    # Loop through each character in the text
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it as it is
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Example usage
text = input("Enter the text to be encrypted: ")
shift = int(input("Enter the shift value: "))

encrypted_text = encrypt(text, shift)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted text: {decrypted_text}")
