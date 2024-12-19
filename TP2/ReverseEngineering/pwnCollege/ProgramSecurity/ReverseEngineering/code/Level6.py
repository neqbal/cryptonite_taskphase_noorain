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

print(key_array)

payload=bytes(key_array)

print(payload)
r.recvuntil(b"Ready to receive your license key!")
r.sendline(payload)

r.interactive()
conn.close()

#sorted_hex_values = sorted(key_array, key=lambda x: int(x, 16))

#print(sorted_hex_values)
