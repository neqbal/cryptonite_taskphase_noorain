
    1498:	48 8d 45 f2          	lea    rax,[rbp-0xe]
    149c:	ba 05 00 00 00       	mov    edx,0x5
    14a1:	48 89 c6             	mov    rsi,rax
    14a4:	bf 00 00 00 00       	mov    edi,0x0
    14a9:	e8 b2 fc ff ff       	call   1160 <read@plt>
    14ae:	c7 45 ec 00 00 00 00 	mov    DWORD PTR [rbp-0x14],0x0
    14b5:	eb 42                	jmp    14f9 <strerror@plt+0x349>
    14b7:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14ba:	48 98                	cdqe
    14bc:	0f b6 44 05 f2       	movzx  eax,BYTE PTR [rbp+rax*1-0xe]
    14c1:	88 45 ea             	mov    BYTE PTR [rbp-0x16],al
    14c4:	b8 04 00 00 00       	mov    eax,0x4
    14c9:	2b 45 ec             	sub    eax,DWORD PTR [rbp-0x14]
    14cc:	48 98                	cdqe
    14ce:	0f b6 44 05 f2       	movzx  eax,BYTE PTR [rbp+rax*1-0xe]
    14d3:	88 45 eb             	mov    BYTE PTR [rbp-0x15],al
    14d6:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14d9:	48 98                	cdqe
    14db:	0f b6 55 eb          	movzx  edx,BYTE PTR [rbp-0x15]
    14df:	88 54 05 f2          	mov    BYTE PTR [rbp+rax*1-0xe],dl
    14e3:	b8 04 00 00 00       	mov    eax,0x4
    14e8:	2b 45 ec             	sub    eax,DWORD PTR [rbp-0x14]
    14eb:	48 98                	cdqe
    14ed:	0f b6 55 ea          	movzx  edx,BYTE PTR [rbp-0x16]
    14f1:	88 54 05 f2          	mov    BYTE PTR [rbp+rax*1-0xe],dl
    14f5:	83 45 ec 01          	add    DWORD PTR [rbp-0x14],0x1
    14f9:	83 7d ec 01          	cmp    DWORD PTR [rbp-0x14],0x1
    14fd:	7e b8                	jle    14b7 <strerror@plt+0x307>

In this code the user input is being reversed using pointer arithmetic 

From `strings` command the expected string is `evsvu`. Reverse this strings `uvsve`

The flag 

    pwn.college{IYVn3j7LbRfe3v-iLadNYxnbrc5.0lN1IDL5kzM1czW}
