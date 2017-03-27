sum = 0

for i in range(1, 1001):
    sum += pow(i, i)
    print(i)

sum = str(sum)[::-1]
sum = sum[:10]
print(sum[::-1])