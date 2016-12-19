# a generator function that generates fibonacci number sequence
def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b

def fibonacci_with_limiter(start_number, end_number):
    for i in fibonacci():
        # if number generated is greater than end number than stop function
        if i > end_number: return
        # while number still meets the requirement, continue
        if i >= start_number:
            yield i

total = 0
for i in fibonacci_with_limiter(1, 4000000):
    if (i % 2 == 0):
        total += i

print total
