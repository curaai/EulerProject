def prime_check(n):
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5)+1, 2):
        if n % i == 0:
            return False

    return True

def goldbach(num):
    global prime_list

    for prime in prime_list:
        temp = num - prime

        for i in range(1, int(temp ** 0.5) + 1):
            if 2 * i ** 2 == temp:
                return True

    return False

if __name__ == '__main__':
    prime_list = [2]

    i = 3
    while True:
        if prime_check(i):
            prime_list.append(i)
        else:
            if goldbach(i) is False:
                print(i)
                break

        i += 2