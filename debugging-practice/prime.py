def is_prime(n):
    if n<2:
        return False
    result = True
    i = 2
    while i< n:
        if n % i == 0:
            result = False
            break
        i = i + 1
    return result

number = 100
for index in range(2, number):
    if number%index == 0:
        if is_prime(index):
            print(index)