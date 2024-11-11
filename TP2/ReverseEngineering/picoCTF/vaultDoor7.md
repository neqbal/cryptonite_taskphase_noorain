### Problem 

Analyze the code and find the flag

```java
    public int[] passwordToIntArray(String hex) {
        int[] x = new int[8];
        byte[] hexBytes = hex.getBytes();
        for (int i=0; i<8; i++) {
            x[i] = hexBytes[i*4]   << 24
                 | hexBytes[i*4+1] << 16
                 | hexBytes[i*4+2] << 8
                 | hexBytes[i*4+3];
        }
        return x;
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        int[] x = passwordToIntArray(password);
        return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734291511
            && x[6] == 960049251
            && x[7] == 1681089078;
    }
```


Its solution is

```java
    int x[] = {1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734291511, 960049251, 1681089078};

        char password[] = new char[32];

        for(int i=0; i<8; i++) {
            password[i*4] = (char) ((x[i] >> 24));
            password[i*4 + 1] = (char) ((x[i] >> 16) & 255);
            password[i*4 + 2] = (char) ((x[i] >> 8) & 255);
            password[i*4 + 3] = (char) (x[i] & 255);
        }

        String s = String.valueOf(password);

        System.out.println("picoCTF{" + s + "}");
```

The flag is `picoCTF{A_b1t_0f_b1t_sh1fTiNg_07990cd3b6}`
