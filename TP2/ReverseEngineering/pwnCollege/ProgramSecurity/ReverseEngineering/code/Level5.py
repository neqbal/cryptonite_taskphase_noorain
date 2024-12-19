from pwn import *

context.arch='amd64'
context.os="linux"

host="pwn.college"
username="hacker"
password="password"
port=22

conn=ssh(user=username, host=host, password=password, port=port)

r = conn.process("/challenge/babyrev-level-5-1")

expected_string = ["10", "0f", "0f", "0d", "15"]
xor_key = "62"

expected_input = []

for i in expected_string:
    expected_input.append(hex(int(i,16) ^ int(xor_key, 16)))

print(expected_input)

payload=""
for i in expected_input:
    payload = payload + i.replace("0x", "\\x")

print(payload)

r.sendline(f"{payload}".encode())

r.interactive()
conn.close()
