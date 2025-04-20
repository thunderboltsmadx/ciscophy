def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces and punctuation unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Just reverse the shift

# Example usage
message = "Hello World"
shift = 3

encrypted = encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)
