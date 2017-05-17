#2017 3.26
def main():
    big = 0
    
    for i in range(1, 100):
        for j in range(1, 100):
            num = pow(i, j)
            str_num = str(num)

            list_sum = sum([int(x) for x  in str_num])
            if list_sum > big:
                big = list_sum

    print(big)

if __name__ == '__main__':
    main()
