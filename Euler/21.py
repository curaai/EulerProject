def d(n):
    res = 0

    for i in range(1, n):
        if n % i == 0:
            res += i

    return res

def main():
    friend_dict = {1: 1}
    friend_list = list()

    for i in range(2, 10000):
        friend_dict[i] = d(i)
        a = friend_dict[i]

        if i == a:
            continue

        try:
            if friend_dict[a] == i:
                friend_list.append(i)
                friend_list.append(a)

        except KeyError:
            continue

    print(sum(friend_list))

main()
