import copy


def prime_check(num):
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) +1, 2):
        if num % i == 0:
            return False

    return True


def permutation(first, end):
    global per_list

    if len(end) == 0:
        per_list.append(first)
    else:
        for i in range(len(end)):
            copy_end = copy.deepcopy(end)

            num = copy_end.pop(i)
            copy_end.sort()

            permutation(first + [num], copy_end)


def fourty_nine(num_list):
    num_list = list(set(num_list))
    num_list.sort()

    if 1487 in num_list:
        return False

    for i in range(1, len(num_list)):

        sub = num_list[i] - num_list[i-1]
        if num_list[i] + sub in num_list:
            if sub < 1000:
                return False

            print("".join(str(x) for x in num_list[i-1:]))
            return True

    return False

if __name__ == '__main__':
    for i in range(1000, 10000):
        if prime_check(i):

            per_list = []
            permutation([], [x for x in str(i)])

            prime_list = [int("".join(x)) for x in per_list if prime_check(int("".join(x))) is True]
            if len(prime_list) >= 3:
                if fourty_nine(prime_list):
                    break