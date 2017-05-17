def is_reverse(num):
    str_num  = str(num)
    reverse_num = str_num[::-1]

    if str_num == reverse_num:
        return True

    return False


def main():
    sum = 0

    for i in range(1, 1000000):

        if is_reverse(i):
            str_i = str(bin(i))[2:]

            if is_reverse(str_i):
                sum += i

    print(sum)

main()