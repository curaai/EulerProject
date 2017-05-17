def multiple(n):
    set_n = set(str(n))

    for mul in range(2, 7):
        compare = set(str(n * mul))

        if not compare == set_n:
            return False

    return True

i = 1

while True:
    i += 1

    if multiple(i):
        break

print(i)
