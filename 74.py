def factorial(n):
    mul = 1
    for i in range(2, n+1):
        mul *= i
    return mul


def factorial_num(n):
    factorialSet = {n}
    res = 0
    count = 0

    while True:
        count += 1

        try:
            res = wholeDict[res]
        except KeyError:
            numList = [int(x) for x in str(n)]
            res = sum(factorialList[x] for x in numList)
            wholeDict[n] = res

        if res in factorialSet:
            return count

        factorialSet.add(res)
        n = res

if __name__ == '__main__':
    factorialList = [factorial(x) for x in range(0, 10)]
    keyList = [x for x in range(0, 10)]
    wholeDict = dict()

    count = 0

    for i in range(1, 1000001):
        if factorial_num(i) == 60:
            print(i)
            count += 1

    print(count)