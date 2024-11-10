# Problem 
Prove that we own CryptoHack.org

The identity of user identified using RSA signature scheme which works like this

Step 1: Sender A uses SHA-1 Message Digest Algorithm to calculate the message digest (MD-1) over the original message M

Step 2: A now encrypts the message digest with its private key. The output of this process is called Digital Signatures (DS) of A

Step 3: Now sender A sends the digital signature along with the origianl message M to B

Step 4: When B receives the original message and digital signature from A, it first uses the same message digest algorithm as was used by A and calculates its own message digest (MD2)

Step 5: Now B uses A's public key to decrypt the digital signature because it was encrypted by A's private key. The result of this process is the origianl Message digest MD1 which was calculated by A

Step 6: If MD1 == MD2, B accepts the original message M as the correct unaltered message from A. It also ensures that the message came from A and not someone else

In this challenge

On the server side, the server uses our provided N and e to verify their signature

```python
    digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
    calculated_digest = pow(SIGNATURE, e, n)
```
Now we can provide n and e so that the calculated_digest is equal to our own message digest
This can be done using simple modular arithemtic

`(a)mod(a-b) = b`

So we write e as 1 and N as `signature - our_message_digest` which will result in calculated_digest = `our_message_digest` 

We can find N using this algorithm 

```python
def perform_attack(signature_hex):
    # Convert hex signature to integer
    signature = int(signature_hex, 16)
    
    # Our malicious message
    malicious_msg = "I am Mallory and I own CryptoHack.org"
    
    # Generate the PKCS1v15 padded digest for our message
    malicious_digest = emsa_pkcs1_v15.encode(malicious_msg.encode(), 256)
    target = bytes_to_long(malicious_digest)
    
    # Calculate N such that SIGNATURE mod N = target
    N = signature - target
    
    # Use e=1 for simplest case
    e = 1
    
    return {
        'option': 'verify',
        'msg': malicious_msg,
        'N': hex(N),
        'e': hex(e)
    }
```

Now we just send the return value to server and we will get our flag 

`crypto{dupl1c4t3_s1gn4tur3_k3y_s3l3ct10n}`
