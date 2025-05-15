def fib(n):
    a, b = 0, 1
    total = 0
    for i in range(n):
        if a % 2 == 0:
            total += a
        a,b = b, a + b
    return total

print(fib(10))
