max = 1001
arrays = [[0 for col in range(max)] for row in range(max)]
center = max//2

num = 1 #1씩 늘어나는 값
expend = 1 #양에서 음으로 바뀔 때 늘어나는 값
flag = 1 #양에서 음으로 바뀌는 값

arrays[center][center] = num
col, row = center, center

while True:
    try:
        for temp in range(2):
            for i in range(1, expend + 1):
                num += 1

                if temp == 0:
                    row = row + 1 * flag
                else:
                    col = col + 1 * flag

                arrays[col][row] = num

        flag *= -1
        expend += 1
    except IndexError:
        break

sum = 0
for i in range(max):
    temp = max -1 - i

    sum += arrays[i][i]
    sum += arrays[temp][i]

print(sum)