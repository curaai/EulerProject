import math

def get_circum(a, b):
    c_2 = pow(a, 2) + pow(b, 2)
    c = math.sqrt(c_2)

    circum = a+b+c

    if circum > 1000:
        return False

    elif circum == int(circum):
        return circum


def main():
    num_list = []
    count_list = []

    for i in range(1, 500):
        for j in range(1, 500):
            res = get_circum(i, j)

            if res is not False:

                if res in num_list:
                    count_list[num_list.index(res)] += 1
                else:
                    num_list.append(res)
                    count_list.append(1)

    big = 0
    index = 0

    for i in range(len(count_list)):
        if big < count_list[i]:
            big = i
            index = i

    print(num_list[index])

main()