    1498:	48 8d 45 f2          	lea    rax,[rbp-0xe]
    149c:	ba 05 00 00 00       	mov    edx,0x5
    14a1:	48 89 c6             	mov    rsi,rax
    14a4:	bf 00 00 00 00       	mov    edi,0x0
    14a9:	e8 b2 fc ff ff       	call   1160 <read@plt>

The user input is at `rbp-0xe`

    14ae:	c7 45 e8 00 00 00 00 	mov    DWORD PTR [rbp-0x18],0x0

A local variable is initialized here 

    14b5:	eb 73                	jmp    152a <strerror@plt+0x37a>
    14b7:	c7 45 ec 00 00 00 00 	mov    DWORD PTR [rbp-0x14],0x0

Second local varaible is initialised
These two local variables are used for counters for the two loops

    14be:	eb 59                	jmp    1519 <strerror@plt+0x369>
    14c0:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14c3:	48 98                	cdqe
    14c5:	0f b6 54 05 f2       	movzx  edx,BYTE PTR [rbp+rax*1-0xe]
    14ca:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
An elements is pushed into the `edx` register 

    14cd:	83 c0 01             	add    eax,0x1
    14d0:	48 98                	cdqe
    14d2:	0f b6 44 05 f2       	movzx  eax,BYTE PTR [rbp+rax*1-0xe]

Its adjacent element is pushed into the `eax` register 

    14d7:	38 c2                	cmp    dl,al
    14d9:	76 3a                	jbe    1515 <strerror@plt+0x365>
    14db:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14de:	48 98                	cdqe
    14e0:	0f b6 44 05 f2       	movzx  eax,BYTE PTR [rbp+rax*1-0xe]
    14e5:	88 45 e6             	mov    BYTE PTR [rbp-0x1a],al
    14e8:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14eb:	83 c0 01             	add    eax,0x1
    14ee:	48 98                	cdqe
    14f0:	0f b6 44 05 f2       	movzx  eax,BYTE PTR [rbp+rax*1-0xe]
    14f5:	88 45 e7             	mov    BYTE PTR [rbp-0x19],al
    14f8:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14fb:	48 98                	cdqe
    14fd:	0f b6 55 e7          	movzx  edx,BYTE PTR [rbp-0x19]
    1501:	88 54 05 f2          	mov    BYTE PTR [rbp+rax*1-0xe],dl
    1505:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    1508:	83 c0 01             	add    eax,0x1
    150b:	48 98                	cdqe
    150d:	0f b6 55 e6          	movzx  edx,BYTE PTR [rbp-0x1a]
    1511:	88 54 05 f2          	mov    BYTE PTR [rbp+rax*1-0xe],dl

They are swapped if `dl <= al` 

    1515:	83 45 ec 01          	add    DWORD PTR [rbp-0x14],0x1
    1519:	b8 04 00 00 00       	mov    eax,0x4
    151e:	2b 45 e8             	sub    eax,DWORD PTR [rbp-0x18]
    1521:	39 45 ec             	cmp    DWORD PTR [rbp-0x14],eax
    1524:	7c 9a                	jl     14c0 <strerror@plt+0x310>
    1526:	83 45 e8 01          	add    DWORD PTR [rbp-0x18],0x1
    152a:	83 7d e8 03          	cmp    DWORD PTR [rbp-0x18],0x3
    152e:	7e 87                	jle    14b7 <strerror@plt+0x307>

The user input is sorted in this level. 
There are two nested loops here and adjacent elements are being compared and swapped.

The sorted array is then compared with `kmrrs`

The flag 

    pwn.college{4N2Nap7xIrRh3rw5MWp1YHzxF3z.0FO1IDL5kzM1czW}
