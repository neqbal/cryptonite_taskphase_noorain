### Problem 

Figure out the output of the assembly code

```ASM
func1:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	cmp	w0, 100
	bls	.L2
	ldr	w0, [x29, 28]
	add	w0, w0, 100
	bl	func2
	b	.L3
.L2:
	ldr	w0, [x29, 28]
	bl	func3
.L3:
	ldp	x29, x30, [sp], 32
	ret
	.size	func1, .-func1
	.align	2
	.global	func2
	.type	func2, %function
```

```python
def func1(w0):
    if w0 <= 100:
        return func3(w0)
    else :
        return func2(w0 + 100)
```

&nbsp;

```ASM
func2:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	cmp	w0, 499
	bhi	.L5
	ldr	w0, [x29, 28]
	sub	w0, w0, #86
	bl	func4
	b	.L6
.L5:
	ldr	w0, [x29, 28]
	add	w0, w0, 13
	bl	func5
.L6:
	ldp	x29, x30, [sp], 32
	ret
	.size	func2, .-func2
	.align	2
	.global	func3
	.type	func3, %function
```

```python
def func2(w0):
    if w0 > 499:
        return func5(w0 + 13)
    else :
        return func4(w0 - 86)
```

&nbsp;

```ASM
func3:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	bl	func7
	ldp	x29, x30, [sp], 32
	ret
	.size	func3, .-func3
	.align	2
	.global	func4
	.type	func4, %function
```

```python
def func3(w0):
    return func7(w0)
```

&nbsp;

```ASM
func4:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	mov	w0, 17
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func1
	str	w0, [x29, 44]
	ldr	w0, [x29, 28]
	ldp	x29, x30, [sp], 48
	ret
```

```python
def func4(w0):
    w0 = 17
    return func1(w0)
```

&nbsp;

```ASM
func5:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	bl	func8
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	ldp	x29, x30, [sp], 32
	ret
```

```python
def func5(w0):
    return func8(w0)
```

&nbsp;

```ASM
func6:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 314
	str	w0, [sp, 24]
	mov	w0, 1932
	str	w0, [sp, 28]
	str	wzr, [sp, 20]
	str	wzr, [sp, 20]
	b	.L14
.L15:
	ldr	w1, [sp, 28]
	mov	w0, 800
	mul	w0, w1, w0
	ldr	w1, [sp, 24]
	udiv	w2, w0, w1
	ldr	w1, [sp, 24]
	mul	w1, w2, w1
	sub	w0, w0, w1
	str	w0, [sp, 12]
	ldr	w0, [sp, 20]
	add	w0, w0, 1
	str	w0, [sp, 20]
.L14:
	ldr	w0, [sp, 20]
	cmp	w0, 899
	bls	.L15
	ldr	w0, [sp, 12]
	add	sp, sp, 32
	ret
```

```python
def func6(w0):
    sp12 = w0
    sp24 = 314
    sp28 = 1932
    sp20 = 0
    while sp20 <= 899:
        w1 = sp28
        w0 = 800
        w0 = w1*w0
        w1 = sp24                        #This is a modulus operation in the first iteration sp12 = 1932*800 - ((1932*800)/314)*314 = (1932*800)%314
        w2 = w0/w1
        w1 = w2*w1
        w0 = w0 - w1
        sp12 = w0
        sp20 = sp20 + 1

    return sp12
```

&nbsp;

```ASM
func7:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	cmp	w0, 100
	bls	.L18
	ldr	w0, [sp, 12]
	b	.L19
.L18:
	mov	w0, 7
.L19:
	add	sp, sp, 16
	ret
```

```python
def func7(w0):
    if w0 <= 100:
        return 7
    else :
        return w0
```

&nbsp;

```ASM
func8:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	add	w0, w0, 2
	add	sp, sp, 16
	ret
```

```python
def func8(w0):
    return w0 + 2
```

Now calling the python func1 
```python
result = hex(func1(3459413018))
print(f"Result: {result}")
```

The output
    Result: 0xce32748d

The flag is `picoCTF{ce32748d}`

