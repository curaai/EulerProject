list = []

for i in range(11, 100):
    for j in range(1, i+1):
        j2 = str(j)
        i2 = str(i)

        for a in j2:
            if a in i2:
                try:
                    div = int(j2.replace(a, ''))
                    vis = int(i2.replace(a, ''))

                    if div/vis == j/i and j != i and a != '0':
                        list.append([j, i])

                except ValueError:
                    pass
                except ZeroDivisionError:
                    pass

numerator = 1
denominator = 1

for i in range(4):
    numerator *= list[i][0]
    denominator *= list[i][1]

print(numerator, denominator)
print(numerator / denominator)