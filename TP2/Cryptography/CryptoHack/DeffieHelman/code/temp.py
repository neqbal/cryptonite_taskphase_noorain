    
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

