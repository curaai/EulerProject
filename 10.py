def isPrime(num):
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

if __name__ == '__main__':
    sum = 2
    for i in range(3, 2000001, 2):
        if isPrime(i) is True:
            sum += i

    print(sum)