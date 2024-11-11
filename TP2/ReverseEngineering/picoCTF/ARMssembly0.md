### Problem 

Figure what the given assembly code is doing when it is provided with two integer arguments

```ARM9
 func1:
	sub	sp, sp, #16
```
`sp` stands for stack pointer \
This line subtracts 16 bytes from the stack pointer to make space for local variables

```ARM9
    str	w0, [sp, 12]
	str	w1, [sp, 8]
```

There are several general purpose register in ARM \
In 64 bit architecture x0 - x30 stands for full 64 bit register and w0 - w30 stands for only the lower half of the 64 bit register ie only 32 bit \

w0-w7 are used to store arguments when calling a function. While w0 is also used to store return value. 

In the above statement w0 contains argument 1 which is being pushed onto the stack (In the higher level language this is equivalent to storing it in a local variable). This is done just to save the arguments since the registers can be used for other purposes also

After this the arguments are again loaded into the register for comparison. 

```ARM9
    cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
```

`cmp` instructions compares the values in the two registers \
If w1 is less than or equal to w0 then it jumps to label .L2. \
If the jump to .L2 was not taken, it loads the first argument back into w0 and jumps to label .L3

```ARM9
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
```

In the L2 it loads the second argument into w0 

and in L3 it restores the stack pointer and returns from the function call

All in all this function compares arg1 and arg2 and if arg2 < arg1 then load arg2 into w0 else dont change the registers and just return

In the main function after the function call, it reads the returned value from w0 register. 

Now as per the question arg1 = 4004594377 and arg2 = 4110761777

This code prints the smallest of the two 

The flag is `picoCTF{f5053f31}`

