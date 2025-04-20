import random

# Function to compute GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclid's Algorithm for modular inverse
def mod_inverse(e, phi):
    def extended_euclid(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    gcd_val, x, _ = extended_euclid(e, phi)
    if gcd_val != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# RSA Key Generation
def generate_keys():
    # Choose two prime numbers
    p = 17
    q = 23
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    # Compute d, the modular inverse of e
    d = mod_inverse(e, phi)

    # Public and Private Keys
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

# RSA Encryption
def encrypt(message, public_key):
    e, n = public_key
    # Convert characters to numbers and encrypt
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

# RSA Decryption
def decrypt(cipher, private_key):
    d, n = private_key
    # Decrypt numbers and convert back to characters
    decrypted = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(decrypted)

# Example usage
public_key, private_key = generate_keys()
message = "HELLO"

print("Original Message:", message)

cipher = encrypt(message, public_key)
print("Encrypted Message:", cipher)

decrypted = decrypt(cipher, private_key)
print("Decrypted Message:", decrypted)
