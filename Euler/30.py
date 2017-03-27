def square(num):
    num = str(num)

    sum = 0
    for i in num:
        i = int(i)
        sum += pow(i, 5)

    return sum


def main():
    res = 0

    for i in range(1000, 250000):
        if i == square(i):
            res += i

    print(res)

main()