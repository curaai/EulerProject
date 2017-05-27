if __name__ == '__main__':
    n = 2

    for i in range(7830456):
        n = (n * 2) % 10000000000

    n = (n * 28433 + 1) % 10000000000
    print(n)

