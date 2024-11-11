#### Problem 

Analyse the code and get the flag 

```java
 public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
        //               
    }
```

We can simply just use the same loops as above on the given string in s.equals and we will get our flag

```java
        String s = "jU5t_a_sna_3lpm18gb41_u_4_mfr340";

        char[] res = new char[32];
        int i;
        for(i=0; i<8; i++) {
            res[i] = s.charAt(i);
        }

        for(;i<16; i++) {
            res[i] = s.charAt(23-i);
        }

        for(; i<32; i++) {
            res[i] = s.charAt(46-i);
        }

        for(i=31; i>=17; i -= 2) {
            res[i] = s.charAt(i);
        }
```

The flag is `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}`
