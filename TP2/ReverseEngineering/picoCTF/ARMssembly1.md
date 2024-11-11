### Problem 

Make the program print 'win' by providing a specific input

```ARM
    sub	sp, sp, #32
	str	w0, [sp, 12] 
	mov	w0, 68
	str	w0, [sp, 16]
	mov	w0, 2
	str	w0, [sp, 20]
	mov	w0, 3
    str	w0, [sp, 24]
```

32 is subtracted from sp to make space for local variables \
Function argument is stored at offset 12 \
68 is stored at offset 16
2 is stored at offset 20
3 is stored at offset 24


```ARM
    ldr	w0, [sp, 20]
	ldr	w1, [sp, 16]
	lsl	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 24]
	sdiv	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	sub	w0, w1, w0
```

load 2 into w0 \
load 68 into w1 \
perform a left shift operation on 68 and store it into w0 \
store w0 at offset 28 (272) \
load 272 into w1 \
load 3 into w0 \
perform a signed divisen 272/3 and store it into w0 (90) \
store 90 at offset 28 \
load 90 into w1 \
load function argument into w0 
subtract w0 from 90 and store it into w0

return 


This function all in all returns 90 - function argument

```ARM
bl	func
	cmp	w0, 0
	bne	.L4
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
```

In the main function if the returned value is 0 then load the contents at .LC0 and print it else load the content from .LC1 and print it

In .LC0 the value stored is 'you win' 

So the argument must 90 

and the flag is `picoCTF{0000005a}`
