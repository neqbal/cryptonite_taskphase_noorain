### Problem 

Analyze the code and find the flag 

```java
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
```

From the code it is clear that that for password to be correct passBytes[i] xor 0x55 = myBytes[i] \
which means passBytes[i] = myBytes[i] xor 0x55

```java
    for(int i=0; i<32; i++) {
            password[i] = (char) (myBytes[i] ^ 0x55);
        }
```

The flag `picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_948b888}`
