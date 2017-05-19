def prime_check(num):
    for i in range(3, int(num ** 0.5) +1 , 2):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    mul = 2
    num = 3

    while True:
        if prime_check(num):
            if mul * num > 1000000:
                break
            mul *= num

        num += 2

    print(mul)