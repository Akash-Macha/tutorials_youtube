# An Armstrong number is a number which is equal to the
# sum of digits raise to the power of total number of digits in the number.
# Ex: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748,...
# 153 = 1^3 + 5^3 + 3^3
# 1. find the length of the given number
# 2. sum
# 3. sum == original number


def is_armstrong(n):
    no_of_digit = len(str(n))
    sum = 0
    temp_n = n
    while temp_n != 0:
        last_digit = temp_n % 10
        sum += (last_digit ** no_of_digit)
        temp_n = temp_n // 10
    if sum == n:
        return True
    return False


if __name__ == '__main__':
    if is_armstrong(8208):
        print("YES")
    else:
        print("NO")
