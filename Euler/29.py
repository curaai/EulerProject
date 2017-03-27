num = set()

for i in range(2, 101):
    for j in range(2, 101):
        num.add(pow(i, j))
        num.add(pow(j, i))

print(len(num))