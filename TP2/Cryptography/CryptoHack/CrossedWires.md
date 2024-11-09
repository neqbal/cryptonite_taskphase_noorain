# Problem

The flag was encrypted by someone else's public key so we need their private key to decrypt it. \
The good thing here is that the prime numbers used by us and the other person is same. \
And since we already know our `d` and `e` we can theoretically compute factors of `N` which will give us `phi` ie `(P-1)(Q-1)` \
Which we can use to create the private exponent of other person by just calculating the inverse of their `e` with `phi` 

```python
    from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long, inverse
    import math
    from gmpy2 import next_prime

    FLAG = b"crypto{????????????????????????????????????????????????}"

    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)
    e = 0x10001
    d = inverse(e, phi)

    my_key = (N, d)

    friends = 5
    friend_keys = [(N, getPrime(17)) for _ in range(friends)]

    cipher = bytes_to_long(FLAG)

    for key in friend_keys:
        cipher = pow(cipher, key[1], key[0])

    print(f"My private key: {my_key}")
    print(f"My Friend's public keys: {friend_keys}")
    print(f"Encrypted flag: {cipher}")
```

This algorithm can be used to find P and Q 

```python
    
    from Crypto.Util.number import GCD
    import math

    def factorize_N(N, e, d):
        # Step 1: Calculate k * φ(N) = e * d - 1
        k_phi = e * d - 1

        # Step 2: Find k and φ(N)
        for k in range(1, 100000):  # Start from a small k and increase
            if k_phi % k == 0:
                phi_N = k_phi // k
                # Step 3: Solve for p and q using N and φ(N)
                # We know that: x^2 - (N - φ(N) + 1)x + N = 0
                a = 1
                b = -(N - phi_N + 1)
                c = N
                discriminant = b * b - 4 * a * c
                if discriminant >= 0:
                    sqrt_discriminant = int(math.isqrt(discriminant))
                    if sqrt_discriminant * sqrt_discriminant == discriminant:
                        # Roots
                        p = (-b + sqrt_discriminant) // (2 * a)
                        q = (-b - sqrt_discriminant) // (2 * a)
                        if p * q == N:
                            return (p, q)

        return None
```


P = 161469718942256895682124261315253003309512855995894840701317251772156087404025170146631429756064534716206164807382734456438092732743677793224010769460318383691408352089793973150914149255603969984103815563896440419666191368964699279209687091969164697704779792586727943470780308857107052647197945528236341228473

Q = 134460556242811604004061671529264401215233974442536870999694816691450423689575549530215841622090861571494882591368883283016107051686642467260643894947947473532769025695530343815260424314855023688439603651834585971233941772580950216838838690315383700689885536546289584980534945897919914730948196240662991266027

phi = 21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280249307490374900729021320924716697863966277266625488626020771604596923670543560857724741855180400786259195735908618899535592322919617065525626834782656528352786625383923291590279348919015437292702452668873586799771898145386750557481851748649545280807708561842706253359025121644739401403945728547286791397492272

Now we can use this algorithm to find the flag

```python

    from Crypto.Util.number import inverse, long_to_bytes

    def multi_layer_rsa_decrypt(ciphertext, my_key, friend_keys, phi):
        """
        Decrypt a ciphertext encrypted multiple times with RSA using different public exponents.

        Parameters:
        - ciphertext: The encrypted message.
        - my_key: A tuple containing (N, d) - the private key.
        - friend_keys: A list of tuples (N, e_i) representing friends' public keys.
        - phi: The Euler's totient of N, used for calculating modular inverses.

        Returns:
        - The decrypted plaintext as bytes.
        """
        N, d = my_key  # Our private key
        decrypted_message = ciphertext

        # Iterate over friend keys in reverse order of encryption
        for N, e_i in reversed(friend_keys):
            d_i = inverse(e_i, phi)  # Calculate the modular inverse for e_i to get d_i
            decrypted_message = pow(decrypted_message, d_i, N)  # Decrypt this layer
    
        # Convert the final decrypted integer message back to bytes
        return long_to_bytes(decrypted_message)
```
The flag is `crypto{3ncrypt_y0ur_s3cr3t_w1th_y0ur_fr1end5_publ1c_k3y}`
