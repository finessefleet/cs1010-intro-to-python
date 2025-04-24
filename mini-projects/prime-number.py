def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

def primes_up_to(n):
    return [x for x in range(2, n+1) if is_prime(x)]

# Example usage:
n = int(input("Enter number: "))
print("Prime" if is_prime(n) else "Not prime")
print("Primes up to", n, ":", primes_up_to(n))
