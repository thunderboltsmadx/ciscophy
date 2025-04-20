# Function to perform modular exponentiation (base^exp mod p)
def power_mod(base, exp, p):
    return pow(base, exp, p)

# Diffie-Hellman key exchange function
def diffie_hellman(p, g, private_key):
    # Compute the public key (g^private_key mod p)
    public_key = power_mod(g, private_key, p)
    return public_key

# Generate the shared secret key (g^other_public_key mod p)
def generate_shared_secret(other_public_key, private_key, p):
    # Compute the shared secret (other_public_key^private_key mod p)
    shared_secret = power_mod(other_public_key, private_key, p)
    return shared_secret

# Example usage:
# Shared prime p and base g
p = 23  # A small prime number (in practice, this should be much larger)
g = 5   # A primitive root mod p

# Alice's private key (randomly chosen)
a_private = 6

# Bob's private key (randomly chosen)
b_private = 15

# Step 1: Alice and Bob compute their public keys
a_public = diffie_hellman(p, g, a_private)
b_public = diffie_hellman(p, g, b_private)

print("Alice's public key:", a_public)
print("Bob's public key:", b_public)

# Step 2: Alice and Bob exchange their public keys

# Step 3: Alice computes the shared secret using Bob's public key
alice_shared_secret = generate_shared_secret(b_public, a_private, p)

# Step 4: Bob computes the shared secret using Alice's public key
bob_shared_secret = generate_shared_secret(a_public, b_private, p)

# Both shared secrets should be the same
print("Alice's shared secret:", alice_shared_secret)
print("Bob's shared secret:", bob_shared_secret)

# Check if both shared secrets are the same
if alice_shared_secret == bob_shared_secret:
    print("Key exchange successful! Shared secret:", alice_shared_secret)
else:
    print("Key exchange failed.")
