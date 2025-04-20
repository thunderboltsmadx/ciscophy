def encrypt(message, key):
    # Create an empty list with 'key' number of strings
    ciphertext = [''] * key

    # Loop through each column index
    for col in range(key):
        pointer = col
        while pointer < len(message):
            # Add the character to the correct column string
            ciphertext[col] += message[pointer]
            # Move pointer to the next row in the same column
            pointer += key

    # Join all column strings into one final encrypted message
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    num_of_columns = len(ciphertext) // key
    if len(ciphertext) % key != 0:
        num_of_columns += 1

    plaintext = [''] * num_of_columns

    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if col == num_of_columns:
            col = 0
            row += 1

    return ''.join(plaintext)

# Example usage
message = "HELLO WORLD"
key = 4

encrypted = encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
