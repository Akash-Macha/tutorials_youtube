# Fibonacci Series
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

n = 15

print('0 1', end=" ")
if n > 2:
    f, s = 0, 1
    while n > 2:
        sum = f + s
        print(sum, end=" ")
        f = s
        s = sum
        n -= 1
