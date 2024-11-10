def calculate_shared_secret(p, alice_public_key, bob_private_key):
    # Calculate the shared secret using Alice's public key and Bob's private key
    shared_secret = pow(alice_public_key, bob_private_key, p)
    return shared_secret

# Example parameters
p = int(input("Enter P"), 16)              # A prime number
alice_public_key = int(input("Enter alice's public key"))  # Alice's public key
bob_private_key = int(input("ENter bob's private key"))  # Bob's private key

# Calculate the shared secret
shared_secret = calculate_shared_secret(p, alice_public_key, bob_private_key)

print(f"Shared Secret: {shared_secret}")
