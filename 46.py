from itertools import count

def prime_check(n):
    if n < 2:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5)+1, 2):
        if n % i == 0:
            return False

    return True


def goldbach(num):
    for i in range(1, num):

        prime = num - 2 * i ** 2
        if prime_check(prime):
            return True

    return False


if __name__ == '__main__':
    for num in count(9, 2):
        if prime_check(num):
            pass
        elif goldbach(num) is False:
            print(num)
            break
