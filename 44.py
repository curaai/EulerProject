def five_num(x):
    return x * (3*x - 1) /2

def is_five(x):
    res = (1 + (1 + 24 * x) ** 0.5) / 6
    if res == round(res):
        return True

    else:
        return False

if __name__ == '__main__':
    i = 2
    five_list = [1]
    flag = 1

    while flag:
        five_list.append(five_num(i))
        i += 1

        for index in range(i-1):
            res = five_list[i-2] + five_list[index]

            if is_five(res) is True:
                if is_five(five_list[i - 2] - five_list[index]) is True:
                    print(abs(five_list[i - 2] - five_list[index]))
                    flag = 0


