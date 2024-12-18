
    1498:	48 8d 45 f2          	lea    rax,[rbp-0xe]
    149c:	ba 05 00 00 00       	mov    edx,0x5
    14a1:	48 89 c6             	mov    rsi,rax
    14a4:	bf 00 00 00 00       	mov    edi,0x0
    14a9:	e8 b2 fc ff ff       	call   1160 <read@plt>
    14ae:	0f b6 45 f2          	movzx  eax,BYTE PTR [rbp-0xe]
    14b2:	88 45 f0             	mov    BYTE PTR [rbp-0x10],al
    14b5:	0f b6 45 f3          	movzx  eax,BYTE PTR [rbp-0xd]
    14b9:	88 45 f1             	mov    BYTE PTR [rbp-0xf],al
    14bc:	0f b6 45 f1          	movzx  eax,BYTE PTR [rbp-0xf]
    14c0:	88 45 f2             	mov    BYTE PTR [rbp-0xe],al
    14c3:	0f b6 45 f0          	movzx  eax,BYTE PTR [rbp-0x10]
    14c7:	88 45 f3             	mov    BYTE PTR [rbp-0xd],al

The input buffer is at `rbp-0xe`

From instruction 14ae to 14c7 the first and second characters are being swapped here

from `strings` command, the expected string is `vojov`. Upon swapping `ovjov`

The flag 

    pwn.college{Qp3GAbwCC64FyllALup9lOt-af9.0FN1IDL5kzM1czW}
