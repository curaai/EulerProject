def permutation(n, r):
    res = 1
    for i in range(n, n-r, -1):
        res *= i
    return res

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


if __name__ == '__main__':
    factorialDict = dict()
    for i in range(2, 101):
        factorialDict[i] = factorial(i)

    count = 0
    for n in range(23, 101):
        for r in range(2, int(n/2)+1):

            res = permutation(n, r) / factorialDict[r]
            if res >= 1000000:
                count += ((int(n/2)+1 - r) * 2)
                if n % 2 == 0: count -= 1

                break

    print(count)
