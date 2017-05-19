import copy


def permutation(first, end):
    if len(end) == 0:
        if fourty_three(first) is True:
            print(first)
            pandigital_list.append(int("".join(str(x) for x in first)))

    else:
        for i in range(len(end)):
            copy_end = copy.deepcopy(end)

            num = copy_end.pop(i)
            copy_end.sort()

            permutation(first + [num], copy_end)


def fourty_three(pandigital):
    for i in range(1, 8):
        num = int("".join(str(x) for x in pandigital[i: i + 3]))
        if not num % prime_list[i - 1] == 0:
            return False

    return True

if __name__ == '__main__':
    per_list = []
    pandigital_list = []
    prime_list = [2, 3, 5, 7, 11, 13, 17]

    permutation([], [x for x in range(0, 10)])
    print(sum(pandigital_list))