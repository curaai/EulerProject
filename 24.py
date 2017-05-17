import copy


def per(first, end):
    global count

    if len(end) == 1:
        count += 1

        if count == 1000000:
            list = first + end
            print(''.join(str(x) for x in list))
    else:
        for i in range(len(end)):
            copy_end = copy.deepcopy(end)

            num = copy_end.pop(i)
            copy_end.sort()

            per(first + [num], copy_end)


if __name__ == '__main__':
    per_list = []

    count = 725760

    temp = [x for x in range(0, 10) if x != 2]
    per([2], temp)
