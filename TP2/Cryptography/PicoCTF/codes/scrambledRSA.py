from pwn import *
import string

r = remote("mercury.picoctf.net", 4257)

r.recvuntil("flag: ")
encrypted_flag = r.recvuntil("\nn: ").decode().strip()
n = r.recvuntil("\ne: ").decode().strip()
e = r.recvuntil("\n").decode().strip()

def remove_segments(result, segments):
    for segment in segments:
        result = result.replace(segment, "")
    return result

known_segments = []
decrypted_flag = ""
while "}" not in decrypted_flag:
    for c in string.printable:
        current_test = decrypted_flag + c
        io.sendlineafter("I will encrypt whatever you give me: ", current_test)
        current_encrypt_test = io.recvuntil("\n").decode().strip()
        current_encrypt_test = current_encrypt_test.replace("Here you go: ", "")

        current_char_rep = remove_segments(current_encrypt_test, known_segments)

        if current_char_rep in encrypted_flag:
            print("New Letter Found: %s+[%s]" % (decrypted_flag, c))
            decrypted_flag += c
            known_segments.append(current_char_rep)
            break

print("Complete Flag: %s" % decrypted_flag)