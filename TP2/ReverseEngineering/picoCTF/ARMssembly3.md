### Problem 

Figure out the output of the given assembly code

```ARM
func1:
	stp	x29, x30, [sp, -48]!     ; stp is store pair, sp - 48 = x29 and sp - 48 + 8 = x30, ! means after this instruction sp = sp - 48
	add	x29, sp, 0               ; x29 = sp + 0
	str	w0, [x29, 28]            ; x29 + 28 = w0 which is the argument
	str	wzr, [x29, 44]           ; x29 + 44 = 0, wzr is a special register which always contains zero
	b	.L2                      ; unconditional jump to .L2
```

This is also called as function prologue. It basically sets up the local variables before moving on to the next instruction

```ARM
.L2:
	ldr	w0, [x29, 28]
	cmp	w0, 0           ; if w0 != 0 jmp to .L4 
	bne	.L4
```

```ARM
.L4:
	ldr	w0, [x29, 28] 
	and	w0, w0, 1       ; AND the LSB of w0 with 1
	cmp	w0, 0           ; if AND operation results in 0 which means jump to .L3 else move to next instruction 
	beq	.L3
	ldr	w0, [x29, 44]
	bl	func2           ; call func2 with x29 + 44 as function argument
	str	w0, [x29, 44]   ; store return value back to x29 + 44
```

```ARM
.L3:
	ldr	w0, [x29, 28]
	lsr	w0, w0, 1         ; performs a right shift operation on w0
	str	w0, [x29, 28]     ; store the new w0 back to stack
```

```ARM
func2:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	add	w0, w0, 3          ; add 3 to W0
	add	sp, sp, 16
	ret
```

The python equivalent of this ARM code is 

```python
def func1(a, b):
    while a != 0:
        if a % 2 != 0:
            b = func2(b)
        a = a >> 1
    return b

def func2(b):
    return b + 3
```

The output of this code is 0x27 \
So flag is `picoCTF{00000027}`
