i = 1
list = []
while True:
    if i > 1000000:
        break

    if len(str(i)) >= 2:
        i = str(i)
        for char in i:
            list.append(int(char))
    else:
        list.append(i)

    i = int(i)
    i += 1

res = 1
for i in range(1, 7):
    num = list[pow(10, i) -1]
    res *= num

print(res)

