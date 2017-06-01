def bouncy(num):
    is_up = False
    is_down = False

    num = [int(x) for x in str(num)]
    for i in range(1, len(num)):
        if num[i-1] < num[i]:
            is_up = True
        elif num[i-1] > num[i]:
            is_down = True

        if is_up == is_down == True:
            return True

    return False

if __name__ == '__main__':
    i = 101
    count = 0

    while count/(i-1) < 0.99:
        if bouncy(i):
            count += 1
        i += 1

    print(i-1)