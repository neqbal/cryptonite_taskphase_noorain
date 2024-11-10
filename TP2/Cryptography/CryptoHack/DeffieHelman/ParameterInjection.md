# Parameter Injection

From the question we know that we can intercept Alice and Bob's communication which means we can change what values are being shared on their channel

Now Alice send's Bob P and G and their generated public key which Bob will use to generate the shared secret key.

So inorder for them to generate to a shared secret key whose value we already know, we can change the value of public key 

The equation used to generate the Shared secret key is (publicKey^privateKey) mod P. 

So we just set the value of public key to 0 which will result in shared secret key to be 0 

    Intercepted from Alice: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0xe22b2cc173c8ba965e6d1e1409a5c2617c45058642821742bf5b4bafb277253398cbd928833c4706f08f5367c98ef2ae804ad8871c12e6a2be72f8e1b088aaeb95b0aa071406f828e8af0dd89343b77ceb52924865f1b7516cd44c2e0dea34a5e8b17393a0b51bc71119332f5f682384047d32250ef21d85edc1e9dc2afebd312d487a74cfa1247de7de1ad2ee020da8cb58272d78fd5ed3ac7e639925fe1c365a670f9d93a005eedbdc3c9161312e828e77b24b75f5e616246c74fd8b640594"}
    Send to Bob: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02","A": "0x0"}
    Intercepted from Bob: {"B": "0x3ec4ca310f4305d51ad56f1cdebd7a3fbed7ed9c381ae29190fabf6b8dbec743c9903dbdc0310bebb95b3782a6fee7a6d2ab3be601489c76b844ce9a36513bcf3d847d9403a0378af0f66cf311f9fbd42704756f2cf0ff97b08a967689e5c19cfa11556e98c1568a2da1ec3541e53563a6300302b707118a15fc04f73cc49b39487fb6b2b2f2350a8d28515fc91dab7d6f086c691ccba6540bd82a7ad3bd340bb5ad510ef72837bf08c044373588da52b32d310e5e5a5ab8cc70f316ea2310f0"}
    Send to Alice: {"B":"0x0"}
    Intercepted from Alice: {"iv": "ff7000cf855b4a5e2e25e2f58d7eb692", "encrypted_flag": "7dd848d73617d027c91b5b4261a7231550c5ad1177c405429c789c3b5b6f00d3"}

Now we use the `decrypt.py` and put the value of shared key as 0 and we will get our flag 

`crypto{n1c3_0n3_m4ll0ry!!!!!!!!}`
