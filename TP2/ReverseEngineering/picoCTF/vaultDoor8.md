### Problem

Analyze the code and get the flag 

```java
    public char[] scramble(String password) { /* Scramble a password by transposing pairs of bits. */
        char[] a = password.toCharArray();
        for (int b = 0; b < a.length; b++) {
            char c = a[b];
            c = switchBits(c, 1, 2);
            c = switchBits(c, 0, 3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */
            c = switchBits(c, 5, 6);
            c = switchBits(c, 4, 7);
            c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
            c = switchBits(c, 3, 4);
            c = switchBits(c, 2, 5);
            c = switchBits(c, 6, 7);
            a[b] = c;
        }
        return a;
    }
```

From the code it is clear that only the bits are shifted. \
So if we just shift the bits in the `char expected[]` array back to their original place we will get our flag \

```java
    public int[] scramble(int arr[]) { /* Scramble a password by transposing pairs of bits. */
        for (int b = 0; b < arr.length; b++) {
            int c = arr[b];
            c = switchBits(c, 6, 7);
            c = switchBits(c, 2, 5);
            c = switchBits(c, 3, 4);
            c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
            c = switchBits(c, 4, 7);
            c = switchBits(c, 5, 6);
            c = switchBits(c, 0, 3);
            c = switchBits(c, 1, 2);
             /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */
            
            arr[b] = c;
        }
        return arr;
    }
```

While reversing the expected array, just reverse the sequence in which the bits are shifted \

The flag is `picoCTF{s0m3_m0r3_b1t_sh1fTiNg_2e762b0ab}`
