def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i

    return res

a = factorial(40)
b = factorial(20)
c = b
d = c * b
print(a/d)