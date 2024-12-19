Unline previous challenge that allowed us to change any 5 addresses, this challenge allows us to change only 1 address

    1efc:	75 14                	jne    1f12 <open@plt+0xca2>

The opcode for this instruction is `75 14`. 
The second byte specifies how many instruction to jump if `ZF` flag is not set
We can change it to 0 

    Changing byte 1/1.
    Offset (hex) to change: 1efd
    New value (hex): 0
    The byte has been changed: *0x5f7a2218fefd = 0.
    Ready to receive your license key!
    
    AA
    Checking the received license key!
    
    You win! Here is your flag:
    pwn.college{opQewZalBO16Y19Qle7TAYhwCTe.0FM3IDL5kzM1czW}
