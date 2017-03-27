def main():
    list = []
    for i in range(2, 50000):
        int_string = add_nums(i)

        if is_pandigital(int_string):
            # print(int_string)
            list.append(int_string)

    big = 0
    for i in list:
        if i > big:
            big = i
    print(big)




def is_pandigital(num):
    num = str(num)
    temp = set()

    # print(num)
    for i in num:
        if i != '0' and i not in temp:
            temp.add(i)
        else:
            return False

    return True


def add_nums(num):
    num_string = str()

    for i in range(1, 6):
        if len(num_string) > 9:
            break

        elif len(num_string) == 9:

            return int(num_string)

        num_string += str(num * i)

    return int(num_string)

main()