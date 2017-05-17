import math

def prime_check(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        elif i > math.sqrt(n):
            return True

def formular(a, b):
    for i in range(0, 1000):
        res = pow(i, 2) + (i * a) + b
        if prime_check(res) is False:
            return i

if __name__ == '__main__':
    big = 0

    max_a, max_b = 0, 0

    for a in range(-999, 1000):
        for b in range(-999, 1000):

            result = formular(a , b)
            if result > big:
                big = result

                max_a = a
                max_b = b

    print(max_a*max_b)