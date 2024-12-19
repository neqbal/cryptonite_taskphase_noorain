
    14b5:	eb 1d                	jmp    14d4 <strerror@plt+0x324>
    14b7:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14ba:	48 98                	cdqe
    14bc:	0f b6 44 05 f2       	movzx  eax,BYTE PTR [rbp+rax*1-0xe]
    14c1:	83 f0 62             	xor    eax,0x62
    14c4:	89 c2                	mov    edx,eax
    14c6:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14c9:	48 98                	cdqe
    14cb:	88 54 05 f2          	mov    BYTE PTR [rbp+rax*1-0xe],dl
    14cf:	90                   	nop
    14d0:	83 45 ec 01          	add    DWORD PTR [rbp-0x14],0x1
    14d4:	83 7d ec 04          	cmp    DWORD PTR [rbp-0x14],0x4

The user input is xorred in this challenge

The string is `150d0f0f10` which is xorred with `0x62`

The answer is `wommr`

The flag 

    pwn.college{k2LFPVRfX1KjKYmv58eFYuPvsZh.0FM2IDL5kzM1czW}
