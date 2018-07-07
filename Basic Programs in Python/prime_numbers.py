# Prime Numbers :
# a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).
import math
'''
Since prime numbers start from 2, we just return True for 2 and 3 (just for simplicity):)
the for num's >3  we check if the numr is divisible by the numbers in the range (2 -> sqrt(number)) (inclusive)
if no number divides the num then we return True, since it is a PRIME Number and vice-vers
'''


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    is_true = True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            is_true = False
            break
    return is_true


def generate_prime(n):
    numbers = []
    for x in range(2, n + 1):
        if is_prime(x):
            numbers.append(x)
    return numbers


if __name__ == '__main__':
    up_to = 50
    prime_numbers = generate_prime(up_to)
    print(prime_numbers)
