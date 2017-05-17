import math

def string_cycle(n):
    n = str(n)

    a = n[-1:]
    b = n[:-1]

    a += b

    return int(a)

def prime_cycle(n):
    limit = len(str(n))
    for i in range(limit):

        n = string_cycle(n)
        if prime_check(n) is False:
            return False

    return True

def prime_check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        elif i > math.sqrt(n):
            return True

if __name__ == '__main__':
    i = 3
    count = 1

    num_list = []
    while i <= 1000000:
        if prime_cycle(i) is True:
            num_list.append(i)
            count += 1

        i += 2

    print(count)