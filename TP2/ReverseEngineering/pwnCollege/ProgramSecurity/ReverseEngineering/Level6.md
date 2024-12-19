I decompiled the binary using ghidra


```c 
  read(0,local_28,0x10);
  bVar1 = local_28[4];
  local_28[4] = local_28[8];
  local_28[8] = bVar1;
  for (local_34 = 0; local_34 < 0xf; local_34 = local_34 + 1) {
    for (local_30 = 0; local_30 < 0xf - local_34; local_30 = local_30 + 1) {
      if (local_28[local_30 + 1] < local_28[local_30]) {
        bVar1 = local_28[local_30];
        local_28[local_30] = local_28[local_30 + 1];
        local_28[local_30 + 1] = bVar1;
      }
    }
  }
  for (local_2c = 0; local_2c < 0x10; local_2c = local_2c + 1) {
    iVar2 = local_2c % 3;
    if (iVar2 == 2) {
      local_28[local_2c] = local_28[local_2c] ^ 0x1e;
    }
    else if (iVar2 < 3) {
      if (iVar2 == 0) {
        local_28[local_2c] = local_28[local_2c] ^ 0x66;
      }
      else if (iVar2 == 1) {
        local_28[local_2c] = local_28[local_2c] ^ 0x5f;
      }
    }
  }
```

The string is `07 3c 7d 05 3b 7b 03 38 77 0d 31 6a 13 29 66 1c`

```python
from pwn import *

context.arch='amd64'
context.os="linux"

host="pwn.college"
username="hacker"
password="password"
port=22

conn=ssh(user=username, host=host, password=password, port=port)

r = conn.process("/challenge/babyrev-level-6-1")

key = "07 3c 7d 05 3b 7b 03 38 77 0d 31 6a 13 29 66 1c".split(" ")
key_array = [int(value.strip(), 16) for value in key]

for i in range(0, len(key)):
    n = i%3

    if n==2:
        key_array[i] = int(key[i], 16) ^ int("1e", 16)
    elif n==1:
        key_array[i] = int(key[i], 16) ^ int("5f", 16)
    elif n==0:
        key_array[i] = int(key[i], 16) ^ int("66", 16)

payload=bytes(key_array)

r.recvuntil(b"Ready to receive your license key!")
r.sendline(payload)

r.interactive()
conn.close()
```

The flag 

    pwn.college{oeo5ZtA9uiv58KM3xhOQDLSvS9p.0lM2IDL5kzM1czW}
