#Bug Focus: Off-by-one error, incorrect logic in condition
#This is a part of CS1010 Code Debugging Sessions started from Week 5. 

def fib(n):
    a, b = 0, 1
    total = 0
    for i in range(n):
        if a % 2 == 1:
            total += a
        a = b
        b = a + b
    return total

print(fib(10))