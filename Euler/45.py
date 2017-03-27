def five(n):
    n = n*(3*n -1)/2
    return n

def six(n):
    n = n*(2*n - 1)
    return n

def three(n):
    n = n*(n+1)/2
    return n

def main():
    i = 2

    three_list = []
    five_list = []
    six_list = []

    state = True
    res = 0

    while state:
        a = three(i)
        three_list.append(three)
        five_list.append(five(i))
        six_list.append(six(i))

        if a in five_list:
            if a in six_list:
                if a > 40755:
                    break

        i += 1

    print(a)

main()
