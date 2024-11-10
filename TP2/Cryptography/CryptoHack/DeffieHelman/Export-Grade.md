# Problem 

Since we can intercept and change the DH key size that both parties will agree on, we choose it to be DH64 since it is easier to work with smaller keys 

    
    Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
    Send to Bob: {"supported":["DH64"]}
    Intercepted from Bob: {"chosen": "DH64"}
    Send to Alice: {"chosen":"DH64"}
    Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x557c6697a1f3912e"}
    Intercepted from Bob: {"B": "0xb602ea79f74a4d9c"}
    Intercepted from Alice: {"iv": "2c20c98a76333ff4b5532a1fb70658f2", "encrypted_flag": "dd691ab2370ee2e9faf5836a721cf053a6e1814fa28125c188cf40fda20b6250"}

Now we can use discrete log calculator to get the private key of Alice (https://www.alpertron.com.ar/DILOG.HTM)

    A = g^a mod P
    a = log g (A) mod P

    g^a≡A(mod P)
    This is read as when g is raised to the power of a and divided by p, the remainder is A
Private key of Alice is `a = 7886425781688647723`

Now we calculate the shared secret using `B^a mod P`

Now we put the shared secret key, iv and cypher_text into decrypt.py and decrypt the cypher

`crypto{d0wn6r4d35_4r3_d4n63r0u5}`
