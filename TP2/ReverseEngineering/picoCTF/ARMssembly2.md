### Problem 

Find out the output of the code when 3848786505 is input

```ARM:
    sub	sp, sp, #32
	str	w0, [sp, 12]
	str	wzr, [sp, 24]
	str	wzr, [sp, 28]
	b	.L2
```

In this code argument is stored at offset 12, \
wzr instruction holds zero so zero is stored at offset 24 and 28 

Next the program jump to label .L2

```ARM
.L2:
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	cmp	w1, w0
	bcc	.L3
	ldr	w0, [sp, 24]
	add	sp, sp, 32
	ret
```

.L2 loads sp(28) and sp(12) into w1 and w2 and compares them \
cmp instruction perform w1 - w0 \
if w1 is less than w0 then the carry flag is set to 0 else it is 1 \
bcc instruction stands for branch if carry clear 

In this code w1 is zero and w1 is the user argument so the branch happens and program jumps to .L3

```ARM
.L3:
	ldr	w0, [sp, 24]
	add	w0, w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 28]
	add	w0, w0, 1
	str	w0, [sp, 28]
```

This code basically does is \
sp(24) = sp(24) + 3 \ 
sp(28) = sp(28) + 1 \

Since .L2 is written after .L3 in the code the program enters .L2 normally and compares the user argument with sp(28) \
if sp(28) is less then argument then again jump to .L3 

This is a loop and it continues till sp(28) is less than argument 

All in all this code adds 3 to sp(24) on each iteration and the iteration happens sp(12) i.e user argument number of times \

So at the end of the iteration sp(24) will have 3*sp(12) 

which is `11546359515` but since the flag can only be 32 bit hexadecimal number we need to truncate it 

```python
>>>print(hex(0x2B03776DB & 0xffffffff))
```

This gives us the flag `0xb03776db`
