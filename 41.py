import copy


def prime_check(num):
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) +1 , 2):
        if num % i == 0:
            return False
    return True


def permutation(first, end):
    global big

    if len(end) == 0:
        res = int("".join([str(x) for x in first]))
        if prime_check(res):

            if res > big:
                big = res

    else:
        for i in range(len(end)):
            copy_end = copy.deepcopy(end)

            num = copy_end.pop(i)
            copy_end.sort()

            permutation(first + [num], copy_end)


if __name__ == '__main__':
    big = 0

    for i in range(4, 10):
        permutation([], [x for x in range(1, i)])

    print(big)