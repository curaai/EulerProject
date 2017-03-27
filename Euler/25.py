first = 1
second = 1
temp = 0
index = 2

limit = int("1"+"0"* 999)
while True:
    temp = first + second

    first = second
    second = temp

    index += 1

    if second >= limit:
        break

print(index)