#Bug Focus: Logical errors, improper loop handling
#This is a part of CS1010 Code Debugging Sessions started from Week 5. 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n[::-1])

for i in range(100, 200):
    if is_prime(i) and is_palindrome(i):
        print(i)
