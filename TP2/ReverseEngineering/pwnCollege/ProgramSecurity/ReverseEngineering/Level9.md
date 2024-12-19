In this challenge the program lets us change the value at any address in the memory 

```c 
  for (local_b4 = 0; local_b4 < 5; local_b4 = local_b4 + 1) {
    printf("Changing byte %d/5.\n",(ulong)(local_b4 + 1));
    printf("Offset (hex) to change: ");
    __isoc99_scanf(&DAT_0010335d,&local_ba);
    printf("New value (hex): ");
    __isoc99_scanf(&DAT_00103373,&local_bb);
    *(byte *)(local_b0 + (ulong)local_ba) = local_bb;
    printf("The byte has been changed: *%p = %hhx.\n",(ulong)local_ba + local_b0,(ulong)local_bb);
  }
```

The program uses MD5 to hash the user input which can never be reversed 

```c 
  read(0,&local_38,0x1b);
  MD5_Init(&local_a8);
  MD5_Update(&local_a8,&local_38,0x1b);
  MD5_Final((uchar *)&local_48,&local_a8);
  memset(&local_38,0,0x1b);
  local_38 = local_48;
  local_30 = local_40;
  puts("Checking the received license key!\n");
  iVar1 = memcmp(&local_38,&DAT_00105010,0x1b);
  if (iVar1 == 0) {
    FUN_00101bd6();
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
```
But we can change the opcodes of if statement and convert it to nop. 

    1fd8:	75 14                	jne    1fee <open@plt+0xd7e>

We can change this to nop

    
    Changing byte 1/5.
    Offset (hex) to change: 1fd8
    New value (hex): 90
    The byte has been changed: *0x639495411fd8 = 90.
    Changing byte 2/5.
    Offset (hex) to change: 1fd9
    New value (hex): 90
    The byte has been changed: *0x639495411fd9 = 90.
    Changing byte 3/5.
    Offset (hex) to change: 0
    New value (hex): 0
    The byte has been changed: *0x639495410000 = 0.
    Changing byte 4/5.
    Offset (hex) to change: 0
    New value (hex): 0
    The byte has been changed: *0x639495410000 = 0.
    Changing byte 5/5.
    Offset (hex) to change: 0
    New value (hex): 0
    The byte has been changed: *0x639495410000 = 0.
    Ready to receive your license key!
    
    AA
    Checking the received license key!
    
    You win! Here is your flag:
    pwn.college{s30tduyw6CCyyh3z_2Nn3EXjASy.0FO2IDL5kzM1czW}
