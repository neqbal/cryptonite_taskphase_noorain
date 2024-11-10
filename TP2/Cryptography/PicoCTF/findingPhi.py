def find_primes(x, n):
    """
    Find p and q given their sum (x) and product (n)
    Using the quadratic formula: p^2 - x*p + n = 0
    """
    # Calculate using quadratic formula
    # p^2 - x*p + n = 0
    # (-(-x) ± sqrt((-x)^2 - 4*1*n)) / 2
    # (x ± sqrt(x^2 - 4n)) / 2
    
    discriminant = x*x - 4*n
    p = (x + pow(discriminant, 1//2)) // 2
    q = n // p
    print(p+q)
    return p, q

def decrypt_flag(x, n, c, e=65537):
    """
    Decrypt RSA ciphertext given x (sum of primes) and n (product of primes)
    """
    # Find the prime factors
    p, q = find_primes(x, n)
    
    # Calculate Euler's totient: φ(n) = (p-1)(q-1)
    phi = (p - 1) * (q - 1)
    
    # Calculate private key d
    d = pow(e, -1, phi)
    
    # Decrypt the message
    m = pow(c, d, n)
    return m

def int_to_bytes(n):
    """Convert an integer to bytes."""
    return n.to_bytes((n.bit_length() + 7) // 8, 'big')

def main():
    # The values from the challenge (in hexadecimal)
    x = int("152a1447b61d023bebab7b1f8bc9d934c2d4b0c8ef7e211dbbcf841136d030e3c829f222cec318f6f624eb529b54bcda848f65574896d70cd6c3460d0c9064cd66e826578c2035ab63da67d069fa302227a9012422d2402f8f0d4495ef66104ebd774f341aa62f493184301debf910ab3d1e72e357a99c460370254f3dfccd9ae", 16)  # Replace with actual x value
    n = int("6fc1b2be753e8f480c8b7576f77d3063906a6a024fe954d7fd01545e8f5b6becc24d70e9a5bc034a4c00e61f8a6176feb7d35fe39c8c03617ea4552840d93aa09469716913b58df677c785cd7633d1b7d31e2222cab53be235aa412ac5c5b07b500cf3fd5d6b91e2ddc51bff1e6eec2cb68723af668df36e10e332a9cbb7f3e2df9593fa0e553ed58afec2aa3bc4ae8ef1140e4779f61bdeae4c0b46136294cf151622e83c3d71b97c815b542208baa28207225f134c5a4feac998aeb178a5552f08643717819c10e8b5ec7715696c3bf4434fbea8e8a516dfd90046a999e24a0fb10d27291eb29ef3f285149c20189e7d0190417991094948180196543b8c91", 16)  # Replace with actual n value
    c = int("16acf84a73cefd321ed491a15c640a495b09050cdce435ec37442faf9a694775e1ebffb6dbad6133cbc54e3f641506b0613f711625594fcb467f915f2708714b4c9936f5f4752c3299157cff4eb68eb82c0054dae351314829974f4feadaf126cda92b97e348dbef2640ec3a729a064e615df73d644700f93bf87579683e253d29622525bea3644f59aac8e0b2553bfea48d99e9b323e03cbf55166659974eb8c51cc7b2c2c5d6aa6c01b056a8ed7283d96656a3496f266726605af1be139d586f208d4d7c59c2771dc8036d490d3672ee4513301002775d7c39eac421c6cb4f01344e061549a4cb11c057accef1726572e447501004c772ec91b4a55811280f", 16)  # Replace with actual c value
    print(x)
    # Decrypt the flag
    decrypted_int = decrypt_flag(x, n, c)
    
    # Convert to bytes and decode
    flag = int_to_bytes(decrypted_int).decode()
    print(f"Decrypted flag: {flag}")

if __name__ == "__main__":
    main()
