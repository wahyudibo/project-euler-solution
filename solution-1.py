total = 0
for number in range(1, 1000):
    # if the number is divisible by 3 or 5 without remainder then sum it with
    # previous number
    if (number % 3 == 0 or number % 5 == 0):
        total = total + number

print total
