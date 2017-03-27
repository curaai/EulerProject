#2017 3.25
def prime_check(n):
    for i in range(3, n, 2):
        if n % i == 0:
            return False

    else:
        return True

def check_move(n):
    long = len(str(n))

    for i in range(1, long):
        a, b = divmod(n, pow(10, i))
        if a not in prime_list or b not in prime_list:
            return False

    return True

if __name__ == '__main__':
    prime_list = [2, 3, 5, 7]

    i = 11
    count = 0

    list = []
    while True:
        if i == 6 or i == 9:
            continue

        if count == 11:
            break

        if prime_check(i):
            prime_list.append(i)

            if check_move(i):
                print(i)
                count += 1
                list.append(i)

        # print(i)
        i += 2

    print(list)
    print(sum(list))