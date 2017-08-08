def sum_of_num(num):
    return sum([int(x) ** 2 for x in str(num)])


def duplication(num):
    global count
    num_set = set()

    while True:
        res = sum_of_num(num)
        if res in one_set:
            one_set.update(num_set)
            break

        elif res in right_set:
            right_set.update(num_set)
            count += 1
            break

        num_set.add(res)
        num = res


if __name__ == '__main__':
    one_set = set([1])
    right_set = set([89])

    count = 0

    for i in range(1, 10000000):
        if i % 100000 == 0:
            print(i)
        duplication(i)

    print(count)
