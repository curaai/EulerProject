def lychrel(n):
    count = 0

    while True:
        if count >= 50:
            return True

        temp = check_reverse(n)
        if temp is not False:
            count += 1
            n = temp
        else:
            return False


def check_reverse(n):
    reverse_n = int(str(n)[::-1])

    res = n + reverse_n
    reverse_res = int(str(res)[::-1])

    if res == reverse_res:
        return False
    else:
        return res

if __name__ == '__main__':
    count = 0

    for i in range(2, 10001):
        if lychrel(i):
            print(i)
            count += 1

    print(count)

