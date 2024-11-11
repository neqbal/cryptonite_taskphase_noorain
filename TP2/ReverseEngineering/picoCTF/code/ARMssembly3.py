a = 3634247936
b = 0

def func1(a, b):
    while a != 0:
        if a % 2 != 0:
            b = func2(b)
        a = a >> 1
    return b

def func2(b):
    return b + 3

print(hex(func1(a, b)))
