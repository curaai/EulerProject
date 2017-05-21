limit = 50000000


def prime_check(num):
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    primeList = [2]
    resultSet = set()

    maxX = int(limit ** 0.5)
    maxY = int(limit ** (1 / 3))
    maxZ = int(limit ** 0.25)

    for i in range(3, maxX + 1, 2):
        if prime_check(i):
            primeList.append(i)

    yIndex = [primeList.index(y) for y in primeList if y > maxY][0]
    zIndex = [primeList.index(z) for z in primeList if z > maxZ][0]

    count = 0
    for x in range(len(primeList)):
        xValue = primeList[x] ** 2
        for y in range(yIndex):

            yValue = primeList[y] ** 3
            if xValue + yValue > limit:
                continue

            for z in range(yIndex):
                zValue = primeList[z] ** 4
                res = zValue + xValue + yValue
                if res < limit:
                    resultSet.add(res)

    print(len(resultSet))