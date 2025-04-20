# Euclid's Algorithm to find GCD
def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclid's Algorithm to find x, y such that ax + by = gcd(a, b)
def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0  # gcd, x, y
    else:
        gcd, x1, y1 = extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Example usage
a = 56
b = 15

print("Using Euclid's Algorithm:")
print(f"GCD of {a} and {b} is {euclid_gcd(a, b)}")

print("\nUsing Extended Euclid's Algorithm:")
gcd, x, y = extended_euclid(a, b)
print(f"GCD: {gcd}")
print(f"x: {x}, y: {y}")
print(f"Verification: {a}*({x}) + {b}*({y}) = {a*x + b*y}")
