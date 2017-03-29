if __name__ == '__main__':
    before = 1
    current = 2
    temp = 0

    sum = current

    while current <= 4000000:
        temp = current
        current += before
        before = temp

        if current % 2 == 0:
            sum += current

    print(sum)