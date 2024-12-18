expected_input = "9d ff 3b 3d 0c f4 49 f2 8a a9 e1 3f 31 39 3f 06 6d d3 43 56 4d 0a 00 50 be 2a 3b c7 c8 eb 3c ce 58 a4 cb e8 9c".split(" ")
hex_expected_input = [hex(int(value.strip(), 16)) for value in expected_input]
print(hex_expected_input)
xor1_key=0xf584f763a791
for i in range(0, len(hex_expected_input)):
    n = i % 6
    if n==0:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("f5", 16)) 
    elif n==1: 
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("84", 16)) 
    elif n==2:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("f7", 16)) 
    elif n==3:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("63", 16)) 
    elif n==4:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("a7", 16)) 
    elif n==5:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("91", 16)) 

print(hex_expected_input)

hex_expected_input[22], hex_expected_input[34] = hex_expected_input[34], hex_expected_input[22]

hex_expected_input.reverse()

hex_expected_input[22], hex_expected_input[31] = hex_expected_input[31], hex_expected_input[22]

for i in range(0, len(hex_expected_input)):
    n = i % 7
    if n==0:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("0f", 16)) 
    elif n==1: 
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("03", 16)) 
    elif n==2:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("d3", 16)) 
    elif n==3:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("a0", 16)) 
    elif n==4:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("c6", 16)) 
    elif n==5:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("2c", 16)) 
    elif n==6:
        hex_expected_input[i] = hex(int(hex_expected_input[i], 16) ^ int("af", 16)) 


for x in hex_expected_input:
    x = x.replace("0x", "\\x")
    print(x, end="")

