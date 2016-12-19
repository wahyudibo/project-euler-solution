import math

def is_prime(n):
    if n <= 1:
        return False

    if n != 2 and n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

# generate sequence of prime number with generator function
def generate_prime_number():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 2 if i > 2 else 1

largest_prime = 0
number = 600851475143
for prime in generate_prime_number():
    if number % prime == 0:
        number /= prime
        largest_prime = prime

    if prime > number:
        break

print largest_prime
