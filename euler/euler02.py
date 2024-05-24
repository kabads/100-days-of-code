# fibonacci sequence

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

a = sum ( x for x in fibonacci(100000) if x % 2 == 0)
print(a)