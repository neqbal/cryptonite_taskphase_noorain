```c 
  MD5_Init(&local_c8);
  for (local_dc = 0; local_dc < local_e0 + -1; local_dc = local_dc + 1) {
    MD5_Update(&local_c8,(void *)((local_dc << 0xc) + local_d0),0x1000);
  }
```

This program stores an MD5 hash of the entire file before we can change any address

```c 
  if (iVar1 == 0) {
    puts("The code\'s integrity is secure!\n");
    local_38 = 0;
    local_30 = 0;
    local_28 = 0;
    local_20 = 0;
    local_1e = 0;
    puts("Ready to receive your license key!\n");
    read(0,&local_38,0x1a);
    MD5_Init(&local_c8);
    MD5_Update(&local_c8,&local_38,0x1a);
    MD5_Final((uchar *)&local_48,&local_c8);
    memset(&local_38,0,0x1a);
    local_38 = local_48;
    local_30 = local_40;
    puts("Checking the received license key!\n");
    iVar1 = memcmp(&local_38,&DAT_00104010,0x1a);
    if (iVar1 == 0) {
      FUN_001017b8();
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
```

We can still change the offsets of if statements to get the flag

The first if condition which checks the intergrity 

    1c01:	0f 85 e0 00 00 00    	jne    1ce7 <open@plt+0xa77>

We can change `85` to `84` then the instruction will `je` instead of `jne`

The second if condition which checks the hash of user input

    1ce3:	75 2c                	jne    1d11 <open@plt+0xaa1>

We can change 2c to 00 which is the offset rip has to go to if `jne` is true 


    Changing byte 1/2.
    Offset (hex) to change: 1c02
    New value (hex): 84
    The byte has been changed: *0x63a496fdec02 = 84.
    Changing byte 2/2.
    Offset (hex) to change: 1ce4
    New value (hex): 0
    The byte has been changed: *0x63a496fdece4 = 0.
    The code's integrity is secure!
    
    Ready to receive your license key!
    
    AA
    Checking the received license key!
    
    You win! Here is your flag:
    pwn.college{UsGBP-2ymJ0KXnDfCgWqRbq3SS_.0lM3IDL5kzM1czW}

