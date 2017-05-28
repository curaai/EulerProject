def check_length(a, b):
    return True if len(str(a)) < len(str(b)) else False


if __name__ == '__main__':
    A = 1
    B = 1
    a = A + B
    b = a + A

    count = 0
    for i in range(0, 1000):

        if check_length(a, b):
            count += 1

        A = a
        B = b
        a = A + B
        b = a + A

    print(count)

"""
연분수 1/2 는 다음과 같은 순열을 가집니다. n번째 분자를 Bn, 분모를 An라고 했을 때
An = An-1 + Bn-1
Bn = An + An-1

이것을 이용하여 만약 len(An) < len(Bn) 이면 카운트 하는 식으로 했습니다.
code 에서는 An 을 a, An-1 을 A로 표현했습니다. (B도 마찬가지)
"""